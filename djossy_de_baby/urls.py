from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_admin.urls')),
    path('profil/', include('profils.urls')),
    path('recrutement/', include('recrutement.urls')),
    path('personnel/', include('personnel.urls')),
    path('comptes/', include('comptes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
