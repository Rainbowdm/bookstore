import uvicorn
from fastapi import FastAPI, Depends, HTTPException

from app.utils.constants import (TOKEN_DESCRIPTION, TOKEN_SUMMARY, REDIS_URL, TESTING,
                                 IS_PRODUCTION, REDIS_URL_PRODUCTION)
from app.routes.v1 import app_v1
from app.routes.v2 import app_v2
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED
from datetime import datetime
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.security import authenticate_user, create_jwt_token, check_jwt_token
from app.models.jwt_user import JWTUser
from app.utils.db_object import db
import app.utils.redis_object as r
import aioredis
from app.utils.redis_object import check_test_redis
import pickle
import logging

app = FastAPI(title="Bookstore API documentation", description="API used for Bookstore", version="1.0.0")
app.include_router(app_v1, prefix="/v1", dependencies=[Depends(check_jwt_token), Depends(check_test_redis)])
app.include_router(app_v2, prefix="/v2", dependencies=[Depends(check_jwt_token), Depends(check_test_redis)])


@app.on_event("startup")
async def connect_db():
    if not TESTING:
        await db.connect()
        if IS_PRODUCTION:
            r.redis = await aioredis.from_url(REDIS_URL_PRODUCTION)
        else:
            r.redis = await aioredis.from_url(REDIS_URL)


@app.on_event("shutdown")
async def disconnect_db():
    if not TESTING:
        await db.disconnect()
        r.redis.close()
        await r.redis.wait_closed()


@app.post("/token", description=TOKEN_DESCRIPTION, summary=TOKEN_SUMMARY)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    redis_key = f"token:{form_data.username}, {form_data.password}"
    user = await r.redis.get(redis_key)
    if not user:
        jwt_user_dict = {"username": form_data.username, "password": form_data.password}
        jwt_user = JWTUser(**jwt_user_dict)
        user = await authenticate_user(jwt_user)
        await r.redis.set(redis_key, pickle.dumps(user))
        if user is None:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    else:
        user = pickle.loads(user)
    jwt_token = create_jwt_token(user)
    return {"access_token": jwt_token}


@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    # modify request
    # if not any(word in str(request.url) for word in ["/token", "docs", "/openapi.json"]):
    #     try:
    #         jwt_token = request.headers["Authorization"].split("Bearer ")[1]
    #         is_valid = check_jwt_token(jwt_token)
    #     except Exception as e:
    #         is_valid = False
    #     if not is_valid:
    #         return Response("Unauthorized", status_code=HTTP_401_UNAUTHORIZED)

    response = await call_next(request)
    # modify response
    execution_time = (datetime.utcnow() - start_time).microseconds
    response.headers["x-execution-time"] = str(execution_time)
    return response


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
