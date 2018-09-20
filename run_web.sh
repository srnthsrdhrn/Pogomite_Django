#!/bin/sh

python manage.py collectstatic --noinput&&python manage.py migrate&&/usr/local/bin/gunicorn Pogomite.wsgi:application --reload -w 2 -b :8000