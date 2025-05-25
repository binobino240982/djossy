from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from personnel.models import Candidature, DemandePersonnel

# ✅ Fonction de vérification pour les accès admin
def est_admin(user):
    return user.is_staff

# --- 1. Accueil public du dashboard ---
def accueil_dashboard(request):
    return render(request, 'gestion_admin/dashboard.html')

# --- 2. Vue admin : Statistiques simples (réservée staff/admin) ---
@staff_member_required
def dashboard(request):
    stats = Candidature.objects.values('statut').annotate(total=Count('id'))
    return render(request, 'gestion_admin/dashboard.html', {'stats': stats})

# --- 3. Vue admin : Statistiques détaillées ---
@login_required
@user_passes_test(est_admin)
def dashboard_admin(request):
    context = {
        'total_candidatures': Candidature.objects.count(),
        'nouvelles': Candidature.objects.filter(statut='nouvelle').count(),
        'en_cours': Candidature.objects.filter(statut='en_cours').count(),
        'accepte': Candidature.objects.filter(statut='acceptee').count(),
        'rejete': Candidature.objects.filter(statut='rejetee').count(),
        'demandes': DemandePersonnel.objects.count(),
        'chart_data': {
            'labels': ['Nouvelles', 'En cours', 'Acceptées', 'Rejetées'],
            'values': [
                Candidature.objects.filter(statut='nouvelle').count(),
                Candidature.objects.filter(statut='en_cours').count(),
                Candidature.objects.filter(statut='acceptee').count(),
                Candidature.objects.filter(statut='rejetee').count()
            ]
        }
    }
    return render(request, 'gestion_admin/dashboard.html', context)

# --- 4. Liste des candidatures (filtrable par statut) ---
@login_required
@user_passes_test(est_admin)
def liste_candidatures(request):
    statut = request.GET.get('statut')
    if statut:
        candidatures_list = Candidature.objects.filter(statut=statut).order_by('-date_postulation')
    else:
        candidatures_list = Candidature.objects.all().order_by('-date_postulation')
    return render(request, 'gestion_admin/liste_candidatures.html', {'candidatures': candidatures_list})

