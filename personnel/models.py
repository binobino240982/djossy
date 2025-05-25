from django.db import models
from django.utils import timezone

class Profil(models.Model):
    nom = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sexe = models.CharField(max_length=10)
    experience = models.TextField()
    competences = models.TextField()
    photo = models.ImageField(upload_to='profils_photos/')
    disponibilite = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

# --- 2. Candidature (employé postulant à une annonce) ---
class Candidature(models.Model):
    STATUT_CHOIX = [
        ('nouvelle', 'Nouvelle'),
        ('en_cours', 'En cours'),
        ('acceptee', 'Acceptée'),
        ('rejetee', 'Rejetée'),
    ]

    statut = models.CharField(max_length=20, choices=STATUT_CHOIX, default='nouvelle')
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(verbose_name="Lettre de motivation / message")
    cv = models.FileField(upload_to='cv/')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    date_postulation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nom} ({self.email})"

# --- 3. Demande de personnel (faite par un employeur) ---
class DemandeEmployeur(models.Model):
    NOM_PERSONNEL_CHOIX = [
        ('Servante', 'Servante'),
        ('Cuisinier', 'Cuisinier'),
        ('Chauffeur', 'Chauffeur'),
        ('Gardien', 'Gardien'),
        ('Autre', 'Autre'),
    ]

    DUREE_CONTRAT_CHOIX = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Mission courte', 'Mission courte'),
    ]

    nom_entreprise = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    type_personnel = models.CharField(max_length=50, choices=NOM_PERSONNEL_CHOIX)
    nombre_personnes = models.PositiveIntegerField()
    lieu_affectation = models.CharField(max_length=100)
    duree_contrat = models.CharField(max_length=50, choices=DUREE_CONTRAT_CHOIX)
    salaire_propose = models.CharField(max_length=50)
    date_debut = models.DateField()
    exigences = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nom_entreprise} - {self.type_personnel}"

# --- 4. Candidature spontanée d’un employé ---
class CandidatureEmploye(models.Model):
    SEXE_CHOIX = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]

    POSTE_CHOIX = [
        ('Servante', 'Servante'),
        ('Cuisinier', 'Cuisinier'),
        ('Chauffeur', 'Chauffeur'),
        ('Gardien', 'Gardien'),
        ('Autre', 'Autre'),
    ]

    EXPERIENCE_CHOIX = [
        ('Débutant', 'Débutant'),
        ('1-2 ans', '1-2 ans'),
        ('3-5 ans', '3-5 ans'),
        ('+5 ans', '+5 ans'),
    ]

    nom_complet = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    sexe = models.CharField(max_length=10, choices=SEXE_CHOIX)
    age = models.PositiveIntegerField()
    poste_recherche = models.CharField(max_length=50, choices=POSTE_CHOIX)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOIX)
    localisation = models.CharField(max_length=100)
    disponibilite = models.DateField()
    cv = models.FileField(upload_to='candidatures/cv/')
    photo = models.ImageField(upload_to='candidatures/photos/')

    def __str__(self):
        return self.nom_complet

# --- 5. Autre type de demande de personnel (facultatif) ---
class DemandePersonnel(models.Model):
    STATUT_CHOIX = [
        ('nouvelle', 'Nouvelle'),
        ('en_traitement', 'En traitement'),
        ('traitee', 'Traitée'),
    ]

    statut = models.CharField(max_length=20, choices=STATUT_CHOIX, default='nouvelle')
    nom_employeur = models.CharField(max_length=100)
    email_employeur = models.EmailField()
    description_poste = models.TextField()
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_employeur} - {self.description_poste[:30]}"
