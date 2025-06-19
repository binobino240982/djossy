from django.urls import path
from . import views

app_name = 'comptes'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    # Autres URLs de l'application comptes
]
