from django.urls import path, include
from api.views.tecnologia_view import TecnologiaList, TecnologiaDetalhes
from api.views.vaga_view import VagaList

urlpatterns = [
    path('tecnologias/', TecnologiaList.as_view(), name='tecnologia-list'),
    path('tecnologias/<int:id>', TecnologiaDetalhes.as_view(), name='tecnologia-detalhes'),
    path('vagas/', VagaList.as_view(), name='vagas-list'),
]