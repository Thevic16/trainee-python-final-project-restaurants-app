FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN pip install --upgrade pip
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip install -r requirements.txt
COPY . .
RUN pip install -e .

CMD gunicorn restaurants_app.wsgi:application --bind 0.0.0.0:8000
