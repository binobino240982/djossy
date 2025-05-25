import os
import django
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djossy_de_baby.settings')
django.setup()

from recrutement.models import Candidature

# Définir l'âge maximum des candidatures
limite = timezone.now() - timedelta(days=90)  # 3 mois

# Récupérer les anciennes candidatures
anciennes = Candidature.objects.filter(date_postulation__lt=limite)
nb_supprimees = anciennes.count()

# Suppression
anciennes.delete()

print(f"🧹 {nb_supprimees} candidatures supprimées (plus vieilles que 3 mois).")
