from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('accueil/', views.accueil_dashboard, name='accueil_dashboard'),
    path('dashboard-detail/', views.dashboard_admin, name='dashboard_admin'),
    path('candidatures/', views.liste_candidatures, name='liste_candidatures'),
]
