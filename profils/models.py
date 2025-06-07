from django.db import models

class Profil(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos_profils/', blank=True, null=True)
    description = models.TextField(blank=True)
    competences = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    disponibilite = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class DemandePersonnel(models.Model):
    nom_entreprise = models.CharField(max_length=150)
    contact_email = models.EmailField()
    contact_telephone = models.CharField(max_length=20)
    description_demande = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Demande de {self.nom_entreprise}"


class Candidature(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cvs_candidatures/')
    lettre_motivation = models.TextField(blank=True)
    date_candidature = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Candidature de {self.nom}"

class ImageUpload(models.Model):
    titre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # Stockée sur Cloudinary

    def __str__(self):
        return self.titre
