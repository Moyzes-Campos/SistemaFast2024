from django.urls import path
from .views import Index, History, Contato

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('sobre', History.as_view(), name='sobre'),
    path('contato', Contato.as_view(), name='contato'),
]
