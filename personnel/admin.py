from django.contrib import admin
from .models import Candidature, DemandePersonnel

# --- Actions rapides pour Candidature ---
@admin.action(description="Marquer comme En cours")
def marquer_en_cours(modeladmin, request, queryset):
    queryset.update(statut='en_cours')

@admin.action(description="Accepter les candidatures sélectionnées")
def accepter_candidatures(modeladmin, request, queryset):
    queryset.update(statut='acceptee')

@admin.action(description="Rejeter les candidatures sélectionnées")
def rejeter_candidatures(modeladmin, request, queryset):
    queryset.update(statut='rejetee')

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'statut', 'date_postulation')  # 'poste_souhaite' supprimé
    list_filter = ('statut', 'date_postulation')
    search_fields = ('nom', 'email')
    ordering = ('-date_postulation',)
    actions = [marquer_en_cours, accepter_candidatures, rejeter_candidatures]

# --- Actions rapides pour DemandePersonnel ---
@admin.action(description="Marquer comme En traitement")
def marquer_en_traitement(modeladmin, request, queryset):
    queryset.update(statut='en_traitement')

@admin.action(description="Marquer comme Traité")
def marquer_traitee(modeladmin, request, queryset):
    queryset.update(statut='traitee')

@admin.register(DemandePersonnel)
class DemandePersonnelAdmin(admin.ModelAdmin):
    list_display = ('nom_employeur', 'statut', 'email_employeur', 'date_demande')
    list_filter = ('statut', 'date_demande')
    search_fields = ('nom_employeur', 'email_employeur')
    ordering = ('-date_demande',)
    actions = ['marquer_en_traitement', 'marquer_traitee']

    @admin.action(description="Marquer comme en traitement")
    def marquer_en_traitement(self, request, queryset):
        queryset.update(statut='En traitement')

    @admin.action(description="Marquer comme traitée")
    def marquer_traitee(self, request, queryset):
        queryset.update(statut='Traitée')
