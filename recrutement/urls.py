from django.urls import path
from . import views

app_name = 'recrutement'

urlpatterns = [
    path('', views.recrutement_accueil, name='recrutement_accueil'),
]
