from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class Utilisateur(AbstractUser):
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)

    ROLE_CHOICES = (
        ('candidat', 'Candidat'),
        ('employeur', 'Employeur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='candidat')

    def __str__(self):
        return f"{self.username} - {self.role}"

Utilisateur = get_user_model()

class Profil(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='profil')
    photo = models.ImageField(upload_to='photos_profils/', blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    competences = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    disponibilite = models.CharField(max_length=100, blank=True)  # ex: "Immédiate", "1 mois", etc.

    def __str__(self):
        return f"Profil de {self.utilisateur.username}"