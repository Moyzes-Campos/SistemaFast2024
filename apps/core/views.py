from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Patrocinador


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['patrocinador'] = Patrocinador.objects.all()
        return context


class History(TemplateView):
    template_name = 'our_history.html'


class Contato(TemplateView):
    template_name = 'contato.html'
