from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.utils.html import format_html
from .models import Utilisateur, Profil

class CustomAdminSite(admin.AdminSite):
    site_header = "Gestion de Placement de Personnes"
    site_title = "Admin Placement"
    index_title = "Tableau de bord"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('stats/', self.admin_view(self.stats_view), name='stats'),
        ]
        return custom_urls + urls

    def stats_view(self, request):
        context = {
            'employeurs_count': Utilisateur.objects.filter(est_employeur=True).count(),
            'candidats_count': Utilisateur.objects.filter(est_candidat=True).count(),
            'profils_count': Profil.objects.count(),
        }
        return TemplateResponse(request, 'admin/stats.html', context)

@admin.action(description="Marquer comme employeur")
def marquer_comme_employeur(modeladmin, request, queryset):
    queryset.update(est_employeur=True)

@admin.action(description="Marquer comme candidat")
def marquer_comme_candidat(modeladmin, request, queryset):
    queryset.update(est_candidat=True)

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'est_employeur', 'est_candidat', 'date_inscription']
    list_filter = ['est_employeur', 'est_candidat', 'date_inscription']
    search_fields = ['username', 'email']
    ordering = ['date_inscription']
    actions = ['envoyer_email', marquer_comme_employeur, marquer_comme_candidat]

    def envoyer_email(self, request, queryset):
        for utilisateur in queryset:
            # Logique pour envoyer un email
            print(f"Email envoyé à {utilisateur.email}")
        self.message_user(request, "Emails envoyés avec succès.")
    envoyer_email.short_description = "Envoyer un email aux utilisateurs sélectionnés"
    envoyer_email.help_text = "Cette action permet d'envoyer un email aux utilisateurs sélectionnés."

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_filter = ['disponibilite']
    search_fields = ['utilisateur__username', 'bio', 'competences', 'experience']

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.photo.url)
        return "Aucune photo"

    def cv_link(self, obj):
        if obj.cv:
            return format_html('<a href="{}" target="_blank">Télécharger</a>', obj.cv.url)
        return "Aucun CV"

admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(Utilisateur, UtilisateurAdmin)
admin_site.register(Profil, ProfilAdmin)