from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import FluxodeCX, Lembrete, Integrantes, ObjetivosArea, Prazos
import datetime
from ..planejamento.models import Sub_Atividades
from django.db.models import Sum
from django.db.models.expressions import F

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index_dash.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['fluxo'] = FluxodeCX.objects.all().order_by('data')
        context['pagina'] = 'Home'
        context['ativo_home'] = 'active'
        usuario = self.request.user
        context['usuario'] = usuario
        areas = ["Aerodinâmica", "Direção", "Eletrica", "Estrutura", "Freio e Ergonomia", "Powertrain",
                 "Comercial", "Financeiro", "Gestão", "Marketing", "Qualidade"]
        area = self.request.path.split("/")[-1]
        context['objetivos'] = ObjetivosArea.objects.all().filter(area=area)
        context['integrantes'] = Integrantes.objects.all().filter(area=area)
        """ Calculo membros por area"""
        tam_areas = []
        for a in areas:
            b = Integrantes.objects.filter(area=a).count()
            tam_areas.append(b)
        context['tam_areas'] = tam_areas

        if area == '':
            context['area'] = 'Geral'
        else:
            context['area'] = area

        tamanho = Sub_Atividades.objects.filter(area=area).count()
        if tamanho > 0:
            tam_AF = Sub_Atividades.objects.filter(area=area).filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = Sub_Atividades.objects.filter(area=area).filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = Sub_Atividades.objects.filter(area=area).filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)


        # Data final
        d1 = datetime.datetime.now()
        d2 = datetime.datetime.strptime('31/07/2024', '%d/%m/%Y')
        dif = abs((d2 - d1).days)
        context['hoje'] = dif

        # Custo Projetado por Área
        custo = Sub_Atividades.objects.filter(area=area).aggregate(Sum('custo'))
        context['custo'] = custo['custo__sum']

        # Retornando os prazos dos principais relatórios

        for a in Prazos.objects.all():
            x = str(a.entrega)
            b = datetime.datetime.strptime(x, '%Y-%m-%d')
            c = datetime.datetime.now()
            a.dias_restantes = abs((b-c).days)
            a.save()
        context['prazos'] = Prazos.objects.all()
        return context
