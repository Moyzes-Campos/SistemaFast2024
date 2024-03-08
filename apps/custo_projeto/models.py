from django.db import models
from ..planejamento.models import Sub_Atividades

"""
class Custo_Area(models.Model):
    area = models.CharField(max_length=100)
    valor = models.DecimalField()
    situacao = models.BooleanField(default=False, help_text='Valor já confirmado?')
    sub_atividade = models.ForeignKey(Sub_Atividades, blank=True, null=True, on_delete=models.SET_NULL)

"""
# Create your models here.
