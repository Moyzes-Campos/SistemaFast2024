from django.urls import path
from .views import Custo_View


urlpatterns = [
    path('', Custo_View.as_view(), name='custo_index'),
]