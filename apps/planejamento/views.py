from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Atividade_Gantt, Sub_Atividades, Gantt_Chart

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'gantt.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pagina'] = 'Gantt Chart'
        context['ativo_dash'] = 'active'
        usuario = self.request.user
        context['usuario'] = usuario

        area = self.request.path.split("/")[-1]
        if area == '':
            context['area'] = 'Geral'
            context['gantt2'] = Gantt_Chart.objects.all().filter(is_atividade=True)
            context['height'] = (Gantt_Chart.objects.all().filter(is_atividade=True).count() * 40) + 40
        else:
            context['area'] = area
            context['gantt2'] = Gantt_Chart.objects.all().filter(area=area).order_by("inicio_atividade", "id_name",
                                                                                     "-is_atividade", "data_inicio")
            context['height'] = (Gantt_Chart.objects.all().filter(area=area).count() * 40) + 40

        return context
