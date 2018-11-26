from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Mascota, Estado, Comuna, Regione, Vivienda, Adoptante

admin.site.site_header = "Mantendeor MisPerris"


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id_mascota', 'nom_mascota', 'tamano_mascota','peso_mascota','color_mascota','fecha_rescate','descripcion','estado')
    list_filter = ('estado',)
    ordering = ('id_mascota',)
    search_fields = ('nom_mascota',)


class RegistroAdoptante(admin.ModelAdmin):
    list_display = ('rut', 'email', 'nombre_full','fec_nac','fono','region','comuna','tipo_vivienda')
    list_filter = ('rut',)
    ordering = ('rut',)
    search_fields = ('nombre_full',)


admin.site.register(Estado)
admin.site.register(Comuna)
admin.site.register(Regione)
admin.site.register(Adoptante,RegistroAdoptante)
admin.site.register(Vivienda)
admin.site.register(Mascota,RegistroAdmin)






