from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index_dash'),
    path('Aerodinamica', IndexView.as_view(), name='indexAE'),
    path('Eletrica', IndexView.as_view(), name='indexEL'),
    path('Direção', IndexView.as_view(), name='indexSP'),
    path('Estrutura', IndexView.as_view(), name='indexES'),
    path('Freio', IndexView.as_view(), name='indexFR'),
    path('Powertrain', IndexView.as_view(), name='indexPW'),
    path('Comercial', IndexView.as_view(), name='indexCM'),
    path('Financeiro', IndexView.as_view(), name='indexFN'),
    path('Gestao_Pessoas', IndexView.as_view(), name='indexGS'),
    path('Marketing', IndexView.as_view(), name='indexMK'),
    path('Qualidade', IndexView.as_view(), name='indexQL'),
]
