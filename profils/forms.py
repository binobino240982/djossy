from django import forms
from .models import DemandePersonnel, Candidature

class DemandePersonnelForm(forms.ModelForm):
    class Meta:
        model = DemandePersonnel
        fields = ['nom_entreprise', 'contact_email', 'contact_telephone', 'description_demande']
        widgets = {
            'description_demande': forms.Textarea(attrs={'rows': 4}),
        }

class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['nom', 'email', 'telephone', 'cv', 'lettre_motivation']
        widgets = {
            'lettre_motivation': forms.Textarea(attrs={'rows': 5}),
        }
