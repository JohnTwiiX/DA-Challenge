#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate

gunicorn todo_project.wsgi:application --bind 0.0.0.0:8000