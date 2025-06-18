from django.urls import path
from . import views

app_name = 'comptes'

urlpatterns = [
    path('login/', views.connexion_utilisateur, name='connexion'),  # URL de connexion (login)
    path('logout/', views.deconnexion_utilisateur, name='deconnexion'),  # Déconnexion

    path('login/', views.connexion_utilisateur, name='connexion'),  # login au lieu de connexion
    path('inscription/', views.inscription_view, name='inscription'),
    path('inscription/employeur/', views.inscription_employeur, name='inscription_employeur'),
    path('inscription/candidat/', views.inscription_candidat, name='inscription_candidat'),
    path('deconnexion/', views.deconnexion_utilisateur, name='deconnexion'),
    
    path('', views.liste_profils, name='liste_profils'),
    path('<int:profil_id>/', views.detail_profil, name='detail_profil'),
]
