from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur, Profil

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ['username', 'email', 'est_employeur', 'est_candidat', 'date_inscription']
    list_filter = ['est_employeur', 'est_candidat', 'is_staff']
    search_fields = ['username', 'email']
    ordering = ['-date_inscription']
    
    # Ajout des champs personnalisés dans l'interface d'administration
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('est_employeur', 'est_candidat', 'date_inscription'),
        }),
    )

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'disponibilite']
    search_fields = ['utilisateur__username', 'competences']
    list_filter = ['disponibilite']