from django.contrib import admin
from .models import New

class NewAdmin(admin.ModelAdmin):
    # Champs à afficher dans la liste des articles
    list_display = ('title', 'author', 'category', 'created_at', 'is_deleted')
    
    # Filtres pour faciliter la navigation
    list_filter = ('category', 'author', 'created_at', 'is_deleted')
    
    # Recherche par titre ou contenu
    search_fields = ('title', 'content')
    
    # Organiser les champs dans le formulaire d'ajout/modification
    fieldsets = (
        ('Informations principales', {
            'fields': ('title', 'sub_title', 'content', 'category', 'author')
        }),
        ('Médias', {
            'fields': ('image', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'video', 'video_url'),
            'description': 'Téléchargez les images et vidéos associées à cet article.'
        }),
        ('Options avancées', {
            'fields': ('is_deleted', 'data'),
            'classes': ('collapse',)  # Masquer par défaut
        }),
    )
    
    # Ajouter des actions personnalisées (ex : marquer comme supprimé)
    actions = ['mark_as_deleted']
    
    def mark_as_deleted(self, request, queryset):
        queryset.update(is_deleted=True)
    mark_as_deleted.short_description = "Marquer comme supprimé"

admin.site.register(New, NewAdmin)



# Register your models here.
