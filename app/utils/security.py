from passlib.context import CryptContext
from app.models.jwt_user import JWTUser
from datetime import datetime, timedelta
from app.utils.constants import JWT_EXPIRATION_TIME_MINUTES, JWT_ALGORITH, JW_SECRET_KEY
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import time
from starlette.status import HTTP_401_UNAUTHORIZED

password_context = CryptContext(schemes=["bcrypt"])
oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")
jwt_user1 = {"username": "user1", "password": "$2b$12$.IJ7XLSIovt7hebPLMBSq.fxDca507nTe1iKd/HR5Y7DUkcKsDRnK",
             "disabled": False, "role": "user"}
fake_jwt_user1 = JWTUser(**jwt_user1)


def get_hashed_password(password):
    return password_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        return password_context.verify(plain_password, hashed_password)
    except Exception as e:
        print(e)
        return False


# Authenticate username and password to give JWT token
def authenticate_user(user: JWTUser):
    if fake_jwt_user1.username == user.username:
        if verify_password(user.password, fake_jwt_user1.password):
            user.role = "admin"
            return user
    return False


# Create access JWT token
def create_jwt_token(user: JWTUser):
    expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    jwt_payload = {"sub": user.username, "role": user.role, "exp": expiration}
    jwt_token = jwt.encode(jwt_payload, JW_SECRET_KEY, algorithm=JWT_ALGORITH)
    return jwt_token


# Check whether JWT token is correct
def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JW_SECRET_KEY, algorithms=JWT_ALGORITH)
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")
        if time.time() < expiration:
            if fake_jwt_user1.username == username:
                return final_checks(role)
    except Exception as e:
        raise False
    raise False


# Last checking and returning the final result
def final_checks(role: str):
    if role == "admin":
        return True
    else:
        return False
