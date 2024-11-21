from django.contrib import admin
from .models import Reclamation

class ReclamationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')  # Affiche ces champs dans la liste
    search_fields = ('title', 'text', 'author__username')  # Permet de rechercher par titre, texte ou auteur

# Enregistrer le modèle avec la personnalisation
admin.site.register(Reclamation, ReclamationAdmin)