from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'role', 'password1', 'password2']

class EmployeurForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.est_employeur = True
        if commit:
            user.save()
        return user

class CandidatForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.est_candidat = True
        if commit:
            user.save()
        return user