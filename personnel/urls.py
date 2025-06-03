from django.urls import path
from . import views

app_name = 'personnel'  # Ajoute un namespace pour éviter les conflits dans les noms d'URL

urlpatterns = [
    path('', views.personnel_accueil, name='personnel_accueil'),
    
    # Pages accessibles à tous
    path('', views.liste_profils, name='liste_profils'),  # Liste tous les profils
    path('<int:profil_id>/', views.detail_profil, name='detail_profil'),  # Détail d'un profil
    path('<int:profil_id>/recruter/', views.recruter, name='recruter'),  # Recruter un profil spécifique
    path('demande/', views.soumettre_demande_personnel, name='soumettre_demande'),  # Formulaire employeurs
    path('postuler/', views.postuler, name='postuler'),  # Formulaire candidats (CV + photo)
    path('candidature/confirmation/', views.confirmation_candidature, name='confirmation_candidature'),

    # Pages réservées à l'administration
    path('admin/candidatures/', views.liste_candidatures, name='liste_candidatures'),
    path('admin/demandes/', views.liste_demandes, name='liste_demandes'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/export/candidatures/', views.exporter_candidatures_csv, name='exporter_candidatures_csv'),

    # Export Excel
    path('export-candidatures/', views.export_candidatures_excel, name='export_candidatures_excel'),
]
