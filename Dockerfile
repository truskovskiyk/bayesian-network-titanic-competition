FROM python:3.6

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get update


ENV APP_DIR /app
WORKDIR $APP_DIR

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . $APP_DIR
