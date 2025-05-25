from django import forms
from .models import (
    Candidature,
    Profil,
    DemandeEmployeur,
    CandidatureEmploye,
    DemandePersonnel,
)

class FormulaireRecrutement(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['nom', 'email', 'telephone', 'message', 'cv', 'photo']

# ✅ Formulaire de base pour postuler à un profil
class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['message', 'cv', 'photo']  # Assure-toi que ces champs existent dans le modèle Candidature

# ✅ Formulaire de demande côté employeur
class DemandeEmployeurForm(forms.ModelForm):
    class Meta:
        model = DemandeEmployeur
        fields = '__all__'
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
        }

# ✅ Formulaire de candidature employé (personnel)
class CandidatureEmployeForm(forms.ModelForm):
    class Meta:
        model = CandidatureEmploye
        fields = '__all__'
        widgets = {
            'disponibilite': forms.DateInput(attrs={'type': 'date'}),
        }

# ✅ Mini-formulaire pour demande rapide de personnel
class DemandePersonnelForm(forms.ModelForm):
    class Meta:
        model = DemandePersonnel
        fields = ['nom_employeur', 'email_employeur', 'description_poste']

class PostulerForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['nom', 'email', 'message', 'cv']  # à adapter selon ton modèle