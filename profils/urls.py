# profils/urls.py

from django.urls import path
from . import views

app_name = 'profils'  # important si tu utilises {% url 'profils:nom_vue' %}

urlpatterns = [
    path('', views.ma_page_profil, name='profil'),
    path('', views.liste_profils, name='liste_profils'),
    path('<int:profil_id>/', views.detail_profil, name='detail_profil'),
    path('<int:profil_id>/recruter/', views.recruter, name='recruter'),
    path('demande/', views.soumettre_demande_personnel, name='soumettre_demande'),
    path('postuler/', views.postuler, name='postuler'),
    path('candidature/confirmation/', views.confirmation_candidature, name='confirmation_candidature'),
    path('admin/candidatures/', views.liste_candidatures, name='liste_candidatures'),
    path('admin/demandes/', views.liste_demandes, name='liste_demandes'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/export/candidatures/', views.exporter_candidatures_csv, name='exporter_candidatures_csv'),
    path('export-candidatures/', views.export_candidatures_excel, name='export_candidatures_excel'),
]
