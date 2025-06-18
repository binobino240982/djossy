from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur, Profil

class InscriptionForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2']

class ConnexionForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Utilisateur.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email

class EmployeurForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
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
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.est_candidat = True
        if commit:
            user.save()
        return user

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['photo', 'cv', 'competences', 'experience', 'disponibilite']
        widgets = {
            'competences': forms.Textarea(attrs={'rows': 4}),
            'experience': forms.Textarea(attrs={'rows': 4}),
        }