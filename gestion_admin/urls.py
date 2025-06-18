from django.urls import path
from . import views

app_name = 'admin_dashboard'  # Changé pour correspondre au namespace

urlpatterns = [
    path('', views.accueil_dashboard, name='accueil'),
    path('dashboard/', views.dashboard_admin, name='dashboard'),
    path('candidatures/', views.liste_candidatures, name='candidatures'),
]
