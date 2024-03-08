from django.contrib import admin

from .models import Atividade_Gantt, Sub_Atividades, Gantt_Chart

class Atividades_Admin(admin.ModelAdmin):
    fields = ['area', 'atividade']
    list_display = ['pk','area','atividade', 'data_inicio', 'data_final', 'situacao']


class Sub_Atividades_Admin(admin.ModelAdmin):
    list_display = ['sub_atividade','atividade','data_inicio','data_final', 'area']
    fields = ['atividade', 'sub_atividade', 'situacao', 'custo', 'data_inicio', 'data_final']



admin.site.register(Atividade_Gantt, Atividades_Admin)
admin.site.register(Sub_Atividades, Sub_Atividades_Admin)
