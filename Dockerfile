FROM python:3.8-alpine

COPY . /app
WORKDIR /app

RUN apk add --virtual .build-deps build-base openssl-dev libffi-dev jpeg-dev zlib-dev && \
    apk add mariadb-connector-c-dev postgresql-dev && \
    pip install pipenv && \
    pipenv install --deploy --system && \
    chmod +x docker-entrypoint.sh && \
    apk --purge del .build-deps

EXPOSE 8000
VOLUME /app/patientportal/settings/config.py

ENTRYPOINT /app/docker-entrypoint.sh