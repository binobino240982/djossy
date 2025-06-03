from django.shortcuts import render

def recrutement_accueil(request):
    return render(request, 'recrutement/accueil.html')

