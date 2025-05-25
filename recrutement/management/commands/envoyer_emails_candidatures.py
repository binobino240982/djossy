from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from recrutement.models import Candidature

class Command(BaseCommand):
    help = "Envoie un email de confirmation aux candidats."

    def handle(self, *args, **kwargs):
        candidatures = Candidature.objects.all()
        compteur = 0

        for c in candidatures:
            if c.email:  # Vérifie que l'email existe
                send_mail(
                    subject="Merci pour votre candidature",
                    message=f"Bonjour {c.nom},\n\nNous avons bien reçu votre candidature. Merci !",
                    from_email="contact@djossydebaby.ci",  # Mets ton adresse ici
                    recipient_list=[c.email],
                    fail_silently=True,
                )
                compteur += 1

        self.stdout.write(self.style.SUCCESS(f"{compteur} emails envoyés."))
