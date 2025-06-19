from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('comptes.urls')),  # URLs de l'application comptes
    path('profils/', include('profils.urls')),
    path('personnel/', include('personnel.urls')),
    path('gestion/', include('gestion_admin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Gestion des erreurs
handler404 = 'comptes.views.custom_404'  # Vue personnalisée pour les erreurs 404
