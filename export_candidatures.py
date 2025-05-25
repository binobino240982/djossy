# export_candidatures.py

import os
import django
import csv
from datetime import datetime

# Configuration de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djossy_de_baby.settings')
django.setup()

from recrutement.models import Candidature  # Adapter si ton app a un nom différent

# Définir le nom du fichier exporté avec la date
nom_fichier = f"candidatures_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Chemin de sauvegarde
chemin_fichier = os.path.join(os.getcwd(), nom_fichier)

# Écriture du fichier CSV
with open(chemin_fichier, mode='w', newline='', encoding='utf-8') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(['Nom', 'Email', 'Téléphone', 'Date de Postulation'])

    for candidature in Candidature.objects.all():
        writer.writerow([
            candidature.nom,
            candidature.email,
            candidature.telephone or '',
            candidature.date_postulation.strftime('%Y-%m-%d %H:%M')
        ])

print(f"✅ Export terminé ! Fichier créé : {chemin_fichier}")
