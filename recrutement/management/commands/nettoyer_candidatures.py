from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from recrutement.models import Candidature

class Command(BaseCommand):
    help = "Supprime les candidatures de plus de 3 mois."

    def handle(self, *args, **kwargs):
        limite = timezone.now() - timedelta(days=90)
        anciennes = Candidature.objects.filter(date_postulation__lt=limite)
        nb = anciennes.count()
        anciennes.delete()
        self.stdout.write(self.style.SUCCESS(f"{nb} candidatures supprimées."))
