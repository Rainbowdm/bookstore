FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

LABEL maintainer="Rainbow"

COPY requirements.txt /
RUN python -m pip install -r /requirements.txt

COPY ./app app
ENV PYTHONPATH=/app
WORKDIR app/