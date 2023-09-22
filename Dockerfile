FROM python:3-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN adduser -u 1000 --disabled-password --gecos "" pingaroo

WORKDIR /app

COPY requirements.txt /app/
RUN apt-get -y update \
    && apt-get -y install git libpq-dev gcc python3-dev \
    && pip install -r requirements.txt \
    && apt-get clean

# Switch to the non-root user
USER pingaroo

# Define the entrypoint command
CMD ["tail", "-F", "somethingsomething"]
