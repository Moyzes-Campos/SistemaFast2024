from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='dash_planejamento'),
    path('Aerodinamica', IndexView.as_view(), name='gantt_AE'),
    path('Eletrica', IndexView.as_view(), name='gantt_EL'),
    path('Estrutura', IndexView.as_view(), name='gantt_ES'),
    path('Freio', IndexView.as_view(), name='gantt_FR'),
    path('Suspensao', IndexView.as_view(), name='gantt_SP'),
    path('Powertrain', IndexView.as_view(), name='gantt_PW'),
    path('Comercial', IndexView.as_view(), name='gantt_CM'),
    path('Financeiro', IndexView.as_view(), name='gantt_FN'),
    path('Gestao_Pessoas', IndexView.as_view(), name='gantt_GS'),
    path('Marketing', IndexView.as_view(), name='gantt_MK'),
    path('Qualidade', IndexView.as_view(), name='gantt_QL'),
]
