FROM python:3.12.3

ENV PYTHONUNBUFFERED=13

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

