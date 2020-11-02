FROM python:3.9.0-alpine
MAINTAINER Senapps Ltd

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /source
WORKDIR /source
COPY ./source /source

RUN adduser -D user
USER user

