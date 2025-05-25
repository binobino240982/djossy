from django.core.management.base import BaseCommand
from recrutement.models import Candidature
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

class Command(BaseCommand):
    help = "Génère un rapport PDF des candidatures"

    def handle(self, *args, **kwargs):
        path = os.path.join("rapports", "rapport_candidatures.pdf")
        os.makedirs("rapports", exist_ok=True)

        c = canvas.Canvas(path, pagesize=A4)
        width, height = A4
        y = height - 50

        candidatures = Candidature.objects.all()
        c.setFont("Helvetica", 12)
        c.drawString(50, y, f"Rapport de {len(candidatures)} candidatures")
        y -= 30

        for i, cand in enumerate(candidatures, start=1):
            if y < 100:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 12)

            ligne = f"{i}. {cand.nom} - {cand.email} - {cand.telephone or 'N/A'}"
            c.drawString(50, y, ligne)
            y -= 20

        c.save()
        self.stdout.write(self.style.SUCCESS("Rapport PDF généré dans le dossier /rapports"))
