from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Profil, Candidature, DemandePersonnel
from .forms import DemandePersonnelForm, CandidatureForm
import csv
import openpyxl  # Assure-toi d’avoir installé openpyxl : pip install openpyxl


def liste_profils(request):
    profils = Profil.objects.all()
    return render(request, 'profils/liste_profils.html', {'profils': profils})


def detail_profil(request, profil_id):
    profil = get_object_or_404(Profil, id=profil_id)
    return render(request, 'profils/detail_profil.html', {'profil': profil})


def recruter(request, profil_id):
    profil = get_object_or_404(Profil, id=profil_id)
    if request.method == 'POST':
        # Ici tu peux gérer un formulaire de recrutement, par exemple
        # Pour l’instant, simple redirection après POST
        return redirect('profils:liste_profils')
    return render(request, 'profils/recruter.html', {'profil': profil})


def soumettre_demande_personnel(request):
    if request.method == 'POST':
        form = DemandePersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profils:liste_profils')
    else:
        form = DemandePersonnelForm()
    return render(request, 'profils/soumettre_demande.html', {'form': form})


def postuler(request):
    if request.method == 'POST':
        form = CandidatureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profils:confirmation_candidature')
    else:
        form = CandidatureForm()
    return render(request, 'profils/postuler.html', {'form': form})


def confirmation_candidature(request):
    return render(request, 'profils/confirmation_candidature.html')


def liste_candidatures(request):
    candidatures = Candidature.objects.all()
    return render(request, 'profils/liste_candidatures.html', {'candidatures': candidatures})


def liste_demandes(request):
    demandes = DemandePersonnel.objects.all()
    return render(request, 'profils/liste_demandes.html', {'demandes': demandes})


def admin_dashboard(request):
    # Tu peux calculer ici des stats ou afficher un résumé
    nb_profils = Profil.objects.count()
    nb_candidatures = Candidature.objects.count()
    nb_demandes = DemandePersonnel.objects.count()
    context = {
        'nb_profils': nb_profils,
        'nb_candidatures': nb_candidatures,
        'nb_demandes': nb_demandes,
    }
    return render(request, 'profils/admin_dashboard.html', context)


def exporter_candidatures_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="candidatures.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Nom', 'Email', 'Téléphone', 'Date de candidature'])

    candidatures = Candidature.objects.all().values_list('id', 'nom', 'email', 'telephone', 'date_candidature')
    for candidature in candidatures:
        writer.writerow(candidature)

    return response


def export_candidatures_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Candidatures"

    headers = ['ID', 'Nom', 'Email', 'Téléphone', 'Date de candidature']
    ws.append(headers)

    candidatures = Candidature.objects.all().values_list('id', 'nom', 'email', 'telephone', 'date_candidature')
    for candidature in candidatures:
        ws.append(candidature)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=candidatures.xlsx'
    wb.save(response)
    return response
