FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

LABEL maintainer="Rainbow"

# install dependencies
COPY requirements.txt /
RUN python -m pip install -r /requirements.txt

COPY . .
# set work directory
WORKDIR /app