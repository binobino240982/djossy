from django.contrib import admin
from .models import Recrutement

@admin.register(Recrutement)
class RecrutementAdmin(admin.ModelAdmin):
    list_display = ['poste', 'employeur', 'candidat', 'date_creation', 'statut']
    list_filter = ['statut', 'date_creation']
    search_fields = ['poste', 'employeur__username', 'candidat__username']
