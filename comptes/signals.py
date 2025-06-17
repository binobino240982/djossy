from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Utilisateur, Profil

@receiver(post_save, sender=Utilisateur)
def creer_profil_utilisateur(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(utilisateur=instance)

@receiver(post_save, sender=Utilisateur)
def sauvegarder_profil_utilisateur(sender, instance, **kwargs):
    instance.profil.save()
