#!/usr/bin/env bash
set -o errexit

# Mise à jour de pip
python -m pip install --upgrade pip

# Installation des dépendances
pip install --no-cache-dir -r requirements.txt

# Nettoyage des fichiers statiques existants
python manage.py collectstatic --no-input --clear

# Migrations de la base de données
python manage.py migrate --noinput
