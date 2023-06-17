from django.contrib import admin
from . import models

# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'create', 'status')

    search_fields = ('tittle', 'create', 'autor', 'visits') 
    readonly_fields = ('visits',)
    fields = ('tittle', 'visits', 'description', 'tags', 'url', 'priority', 'content', 'image', 'alt_image', 'autor', 'status')
    

admin.site.register(models.Articulo, ArticuloAdmin)