FROM python:3.10

# set work directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy project
COPY ./app /code/app

#  run the uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]