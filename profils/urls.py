from django.urls import path
from . import views
from .views import creer_profil

urlpatterns = [
    path('ajouter/', creer_profil, name='creer_profil'),
    path('success/', lambda request: render(request, 'profils/success.html'), name='profil_success'),
]

app_name = 'profils'

urlpatterns = [
     path('', views.profil_accueil, name='profil_accueil'),  # Page d’accueil (accueil du site)
     
    # Autres pages spécifiques
    path('mon-profil/', views.ma_page_profil, name='profil'),
    path('liste/', views.liste_profils, name='liste_profils'),
    path('<int:profil_id>/', views.detail_profil, name='detail_profil'),
    path('<int:profil_id>/recruter/', views.recruter, name='recruter'),

    # Recrutement
    path('demande/', views.soumettre_demande_personnel, name='soumettre_demande'),
    path('postuler/', views.postuler, name='postuler'),
    path('candidature/confirmation/', views.confirmation_candidature, name='confirmation_candidature'),

    # Admin
    path('admin/candidatures/', views.liste_candidatures, name='liste_candidatures'),
    path('admin/demandes/', views.liste_demandes, name='liste_demandes'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Export
    path('admin/export/candidatures/', views.exporter_candidatures_csv, name='exporter_candidatures_csv'),
    path('admin/export/excel/', views.export_candidatures_excel, name='export_candidatures_excel'),
    
    path('upload-test/', upload_image, name='upload_image'),
    
    ath('ajouter/', creer_profil, name='creer_profil'),
    path('success/', lambda request: render(request, 'profils/success.html'), name='profil_success'),
    
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/', views.upload_success, name='upload_success'),
]
