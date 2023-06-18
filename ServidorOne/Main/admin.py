from django.contrib import admin
from .models import Portafolio, Habilidades, Certificaciones, Proyectos

# Register your models here.
admin.site.site_header = 'estuardodev'
admin.site.index_title = 'Panel de control de mi sitio'
admin.site.site_title = 'Administrador'

class PortafolioAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    fields = ('imagen', 'texto_largo')

admin.site.register(Portafolio, PortafolioAdmin)

class HabilidadesAdmin(admin.ModelAdmin):
    list_display = ('descHabilidad',)
    fields = ('descHabilidad',)

admin.site.register(Habilidades, HabilidadesAdmin)

class CertificacionesAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    fields = ('titulo', 'descripcion', 'enlace', 'imagen')

admin.site.register(Certificaciones, CertificacionesAdmin)

class ProyectosAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    fields = ('titulo', 'descripcion', 'texto_enlace', 'enlace', 'imagen', 'alt_imagen')

admin.site.register(Proyectos, ProyectosAdmin)
