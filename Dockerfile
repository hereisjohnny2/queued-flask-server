FROM python:3.8-alpine

COPY requirements.txt /usr/src

WORKDIR /usr/src

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .