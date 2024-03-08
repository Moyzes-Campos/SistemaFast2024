from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import TemplateView
from ..planejamento.models import Sub_Atividades
from django.db.models import Sum


# Create your views here.
class Custo_View(TemplateView):
    template_name = 'custo_projetos.html'

    def get_context_data(self, **kwargs):
        context = super(Custo_View, self).get_context_data(**kwargs)
        context['custo_por_area'] = Sub_Atividades.objects.values('area').annotate(Sum('custo'))
        context['pagina'] = 'Custos_Projeto'
        context['ativo_custo'] = 'active'
        usuario = self.request.user
        context['usuario'] = usuario
        return context
