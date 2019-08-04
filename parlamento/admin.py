from django.contrib import admin
from parlamento.models import Diputado, Entidad, Partido, Iniciativa
from django.utils.html import format_html

# Register your models here.


@admin.register(Iniciativa)
class IniciativaAdmin(admin.ModelAdmin):
    list_display = ['sinopsis']
@admin.register(Entidad, Partido)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Diputado)
class DiputadoAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img width="20" src="{}">'.format(obj.image.url))
    list_display = ['id', 'image_tag', 'name', 'email', 'partido', 'entidad']
