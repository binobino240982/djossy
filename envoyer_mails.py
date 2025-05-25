import os
import django
from django.core.mail import send_mail
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djossy_de_baby.settings')
django.setup()

from recrutement.models import Candidature

# Exemple : on envoie un email aux 5 dernières candidatures
candidats = Candidature.objects.order_by('-date_postulation')[:5]

for candidat in candidats:
    send_mail(
        subject='Confirmation de votre candidature',
        message=f"Bonjour {candidat.nom},\n\nNous avons bien reçu votre candidature. Merci de postuler à DJÔSSY DE BABY.\n\nCordialement,\nL'équipe",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[candidat.email],
        fail_silently=False
    )
    print(f"📧 Email envoyé à {candidat.email}")
