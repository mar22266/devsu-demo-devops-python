#!/bin/sh
set -e

python manage.py migrate --noinput

gunicorn demo.wsgi:application --bind 0.0.0.0:8000
