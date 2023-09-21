FROM python:3-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
COPY . /app/
RUN adduser -u 1000 --disabled-password --gecos "" pingaroo && chown -R pingaroo /app
USER pingaroo

COPY --chown=pingaroo local_settings.py.tpl /app/local_settings.py
ENV DJANGO_SETTINGS_MODULE=local_settings
USER root
RUN apt-get -y update
RUN apt-get -y install git libpq-dev gcc python3-dev
USER pingaroo
RUN pip install -r requirements.txt
