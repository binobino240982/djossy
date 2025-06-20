from django.urls import path
from . import views

app_name = 'comptes'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('inscription/', views.inscription_view, name='inscription'),
    path('profil/editer/', views.editer_profil, name='editer_profil'),
]
