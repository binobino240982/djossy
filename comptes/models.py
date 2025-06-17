from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator

class Utilisateur(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Adresse email')
    est_employeur = models.BooleanField(default=False, verbose_name='Est un employeur')
    est_candidat = models.BooleanField(default=False, verbose_name='Est un candidat')
    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return self.username

class Profil(models.Model):
    utilisateur = models.OneToOneField(
        Utilisateur, 
        on_delete=models.CASCADE, 
        related_name='profil',
        verbose_name='Utilisateur'
    )
    bio = models.TextField(
        blank=True, 
        null=True, 
        verbose_name='Biographie',
        help_text='Décrivez-vous en quelques mots'
    )
    photo = models.ImageField(
        upload_to='photos_profils/', 
        blank=True, 
        null=True,
        verbose_name='Photo de profil',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
        help_text='Formats acceptés : JPG, JPEG, PNG'
    )
    cv = models.FileField(
        upload_to='cvs/', 
        blank=True, 
        null=True,
        verbose_name='CV',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])],
        help_text='Formats acceptés : PDF, DOC, DOCX'
    )
    competences = models.TextField(
        blank=True,
        verbose_name='Compétences',
        help_text='Listez vos compétences principales'
    )
    experience = models.TextField(
        blank=True,
        verbose_name='Expérience professionnelle',
        help_text='Décrivez votre expérience professionnelle'
    )
    disponibilite = models.CharField(
        max_length=100, 
        blank=True,
        verbose_name='Disponibilité',
        help_text='Ex: Immédiate, Dans 3 mois, etc.'
    )

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profils'

    def __str__(self):
        return f"Profil de {self.utilisateur.username}"