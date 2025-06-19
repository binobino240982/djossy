#!/usr/bin/env bash
set -o errexit

# Installing dependencies
pip install --no-cache-dir -r requirements.txt
pip install --no-cache-dir psycopg2-binary

# Running migrations
python manage.py migrate

# Collecting static files
python manage.py collectstatic --no-input --clear
