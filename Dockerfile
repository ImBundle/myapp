FROM python:3.5-slim
ENV PYTHONUNBUFFERED 1
MAINTAINER Davide Davin <davidedvn@gmail.com>

RUN apt-get update && apt-get install -qq -y build-essential libpq-dev --fix-missing --no-install-recommends

ENV INSTALL_PATH /myproject
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
