from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Utilisateur
from .forms import InscriptionForm
from django.contrib.auth.decorators import login_required
from .models import Profil
from django.shortcuts import get_object_or_404

def detail_profil(request, profil_id):
    profil = get_object_or_404(Profil, pk=profil_id)
    return render(request, 'profils/detail_profil.html', {'profil': profil})

def liste_profils(request):
    profils = Profil.objects.all()
    return render(request, 'profils/liste_profils.html', {'profils': profils})

# === Formulaires personnalisés ===

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

# === Vues ===

def inscription_view(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            login(request, utilisateur)
            return redirect('liste_profils')  # Redirection par défaut
    else:
        form = InscriptionForm()
    return render(request, 'comptes/inscription.html', {'form': form})


def inscription_employeur(request):
    if request.method == 'POST':
        form = EmployeurForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Compte employeur créé avec succès.")
            return redirect('liste_profils')
    else:
        form = EmployeurForm()
    return render(request, 'comptes/inscription_employeur.html', {'form': form})


def inscription_candidat(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Compte candidat créé avec succès.")
            return redirect('liste_profils')
    else:
        form = CandidatForm()
    return render(request, 'comptes/inscription_candidat.html', {'form': form})


def connexion_utilisateur(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            utilisateur = form.get_user()
            login(request, utilisateur)
            messages.success(request, f"Bienvenue {utilisateur.username} !")
            
            # Redirection selon le rôle
            if utilisateur.est_employeur:
                return redirect('soumettre_demande_personnel')
            elif utilisateur.est_candidat:
                return redirect('liste_profils')
            else:
                return redirect('accueil')
    else:
        form = AuthenticationForm()
    return render(request, 'comptes/connexion.html', {'form': form})


def deconnexion_utilisateur(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('connexion')
