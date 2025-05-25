import os
import django
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djossy_de_baby.settings')
django.setup()

from recrutement.models import Candidature

fichier_pdf = f"rapport_candidatures_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
chemin = os.path.join(os.getcwd(), fichier_pdf)

c = canvas.Canvas(chemin, pagesize=A4)
largeur, hauteur = A4

y = hauteur - 50
c.setFont("Helvetica-Bold", 14)
c.drawString(50, y, "Rapport des candidatures")
y -= 30
c.setFont("Helvetica", 10)

for candidature in Candidature.objects.all():
    ligne = f"{candidature.nom} | {candidature.email} | {candidature.telephone} | {candidature.date_postulation.strftime('%d/%m/%Y')}"
    c.drawString(50, y, ligne)
    y -= 15
    if y < 50:
        c.showPage()
        y = hauteur - 50

c.save()
print(f"📄 Rapport PDF généré : {chemin}")
