FROM python:3.11.7-bookworm

LABEL maintainer="alfredomorais"

WORKDIR /src
COPY . /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN apt-get update && \
  apt-get install -y --no-install-recommends

RUN pip3 install -r requirements.txt
