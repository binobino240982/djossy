#!/usr/bin/env bash
# Script pour préparer Render

echo "🔧 Collecting static files..."
python manage.py collectstatic --noinput
