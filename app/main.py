import uvicorn
from fastapi import FastAPI
from routes.v1 import app_v1
from routes.v2 import app_v2

app = FastAPI()
app.mount("/v1", app_v1)
app.mount("/v2", app_v2)

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
