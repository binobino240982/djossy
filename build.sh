#!/usr/bin/env bash
set -o errexit

# Mise à jour de pip et installation des dépendances
python -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

# Nettoyage et collecte des fichiers statiques
python manage.py collectstatic --no-input --clear

# Application des migrations
python manage.py migrate --noinput
