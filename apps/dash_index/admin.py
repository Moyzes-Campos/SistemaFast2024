from django.contrib import admin
# Register your models here.
from .models import ObjetivosArea, FluxodeCX, Integrantes, Prazos


admin.site.register(ObjetivosArea)
admin.site.register(FluxodeCX)
admin.site.register(Integrantes)


class Prazos_Admin(admin.ModelAdmin):
    list_display = ['titulo', 'entrega']


admin.site.register(Prazos, Prazos_Admin)
