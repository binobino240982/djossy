from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ImageUploadForm
from .forms import ProfilForm

def creer_profil(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profil_success')
    else:
        form = ProfilForm()
    return render(request, 'profils/creer_profil.html', {'form': form})

# Vue d’accueil
def profil_accueil(request):
    return render(request, 'profils/accueil.html')

# Profil utilisateur
def ma_page_profil(request):
    return render(request, 'profils/mon_profil.html')

# Liste des profils
def liste_profils(request):
    return render(request, 'profils/liste_profils.html')

# Détail d’un profil
def detail_profil(request, profil_id):
    return render(request, 'profils/detail_profil.html', {'profil_id': profil_id})

# Recrutement d’un profil
def recruter(request, profil_id):
    return render(request, 'profils/recruter.html', {'profil_id': profil_id})

# Soumettre une demande de personnel
def soumettre_demande_personnel(request):
    return render(request, 'profils/soumettre_demande.html')

# Postuler à une offre
def postuler(request):
    return render(request, 'profils/postuler.html')

# Confirmation de candidature
def confirmation_candidature(request):
    return render(request, 'profils/confirmation_candidature.html')

# Liste des candidatures (admin)
def liste_candidatures(request):
    return render(request, 'profils/admin/liste_candidatures.html')

# Liste des demandes de personnel (admin)
def liste_demandes(request):
    return render(request, 'profils/admin/liste_demandes.html')

# Tableau de bord admin
def admin_dashboard(request):
    return render(request, 'profils/admin/dashboard.html')

# Exporter les candidatures en CSV
def exporter_candidatures_csv(request):
    return HttpResponse("Export CSV - à implémenter")

# Exporter les candidatures en Excel
def export_candidatures_excel(request):
    return HttpResponse("Export Excel - à implémenter")

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')