# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from parlamento.models import Diputado, Entidad, Partido

# Register your models here.


@admin.register(Entidad, Partido, Diputado)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name']
