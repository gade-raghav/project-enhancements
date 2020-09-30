# Base image
FROM python:3.6-alpine

# Workdir
WORKDIR /app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# Copy Project
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# collect static files
RUN python manage.py collectstatic --noinput


# run gunicorn
CMD gunicorn enhancements.wsgi:application --bind 0.0.0.0:$PORT
