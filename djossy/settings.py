"""
Django settings for djossy project.
Version corrigée - sécurisée pour développement
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# 1. Chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. 🔑 CORRECTION CLAÉ SECRÈTE (le problème principal)
# Génère une clé temporaire pour développement (à remplacer en production)
SECRET_KEY = "django-insecure-dvlop!tmp_ke7&9mz(9^$j4%f8h!@a3*bc_angerevel240982"  # ⚠️ Temporaire!

# 3. Mode débogage - À PASSER À FALSE EN PRODUCTION!
DEBUG = True  

# 4. Hôtes autorisés - À MODIFIER EN PRODUCTION
ALLOWED_HOSTS = ['*']  # ❗ Remplacer par votre domaine réel en prod

# 5. Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Vos applications
    'personnel',
    'comptes',
    'profils',
    'gestion_admin',
    'recrutement',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# 6. Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Pour les fichiers statiques
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 7. Configuration des URLs
ROOT_URLCONF = 'djossy.urls'

# 8. Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 9. Application WSGI
WSGI_APPLICATION = 'djossy.wsgi.application'

# 10. 🛑 CORRECTION BASE DE DONNÉES 
# Externalisation des identifiants (plus sécurisé)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='djossy_db'),  # Utilise .env
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# 11. Validateurs de mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 12. Internationalisation
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 13. Fichiers statiques
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # ✅ Ajout important

# 14. Fichiers média
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 15. Configuration email (exemple pour Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='votre@gmail.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='votre-mot-de-passe-app')

# 16. Modèle utilisateur personnalisé
AUTH_USER_MODEL = 'comptes.Utilisateur'

# 17. Champ auto par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 18. Configuration Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', default=''),
    'API_KEY': config('CLOUDINARY_API_KEY', default=''),
    'API_SECRET': config('CLOUDINARY_API_SECRET', default=''),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'