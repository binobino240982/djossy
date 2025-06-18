from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from gestion_admin.views import accueil_dashboard  # Vue d'accueil publique
from comptes.models import Utilisateur

urlpatterns = [
    path('admin/', admin.site.urls),

    # Page d'accueil publique (remplace le site par défaut)
    path('', accueil_dashboard, name='accueil_dashboard'),
    path('', views.accueil, name='accueil'),

    # Applications
    path('admin-panel/', include('gestion_admin.urls')),
    path('profil/', include('profils.urls')),
    path('recrutement/', include('recrutement.urls')),
    path('', include('gestion_admin.urls')),  # URLs de l'app gestion_admin
    path('personnel/', include('personnel.urls')),
    path('comptes/', include('comptes.urls')),

    # Exemple : si tu veux une app spéciale pour le tableau de bord
    # path('dashboard/', include('dashboard.urls')),
]

# Pour gérer les fichiers médias en mode DEBUG (photos, CV, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

utilisateur = Utilisateur.objects.get(email='email_en_conflit')
utilisateur.email = 'nouveau_email_unique@example.com'
utilisateur.save()
