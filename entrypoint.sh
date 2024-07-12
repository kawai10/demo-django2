#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py makemigrations --merge
python manage.py migrate --noinput

echo "${0}: collecting statics."

python manage.py collectstatic --noinput

gunicorn config.wsgi:application \
    --bind 0.0.0.0:5000 \
    --log-level=info \
    --reload