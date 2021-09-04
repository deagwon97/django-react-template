# pull official base image
FROM python:3.8-slim-buster

#set environment variables
# I don't want to generate pcy files
ENV PYTHONDONTWRITEBYTECODE 1
# ignore buffering
ENV PYTHONUNBUFFERED 1
# set encoding
ENV PPYTHONENCODING utf-8

#set work directory
WORKDIR /workdir

#for mysql
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

#install dependencies
COPY backend/requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
