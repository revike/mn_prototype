#!/bin/sh

# shellcheck disable=SC2164
cd backend

python3 manage.py migrate
python3 manage.py create_users
#python3 manage.py runserver 0.0.0.0:8000
gunicorn backend.wsgi -b 0.0.0.0:8080
