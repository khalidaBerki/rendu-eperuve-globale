from django.contrib import admin
from .models import Adherent, ResponsableLegal, Intervenant

@admin.register(Adherent)
class AdherentAdmin(admin.ModelAdmin):
    list_display = ['nom', 'age', 'statut_cotisation', 'badge_id', 'cours_id']
    list_filter = ['statut_cotisation']
    search_fields = ['nom', 'badge_id']

@admin.register(ResponsableLegal)
class ResponsableLegalAdmin(admin.ModelAdmin):
    list_display = ['nom', 'relation', 'email', 'telephone']
    search_fields = ['nom', 'email']


@admin.register(Intervenant)
class IntervenantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'role', 'telephone', 'cours_id')  # Utilisez les noms de champs corrects du modèle Intervenant
    search_fields = ('nom', 'role')