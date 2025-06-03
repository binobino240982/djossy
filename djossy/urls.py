from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gestion_admin.views import accueil_dashboard  # Vue d'accueil publique

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # On inclut les URLs de l'app main
    path('', accueil_dashboard, name='accueil_dashboard'),  # Page d’accueil publique

    path('admin-panel/', include('gestion_admin.urls')),     # Dashboard admin
    path('profils/', include('profils.urls')),               # Affichage des profils
    path('comptes/', include('comptes.urls')),               # Connexion / inscription
    path('recrutement/', include('personnel.urls')),         # Candidatures et demandes
]

# Fichiers média (photos, CV, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
