from django.urls import path, include
from .views import tecnologia_view

urlpatterns = [
    path('tecnologias/', tecnologia_view.TecnologiaList.as_view(), name='tecnologia-list'),
    path('tecnologias/<int:id>', tecnologia_view.TecnologiaDetalhes.as_view(), name='tecnologia-detalhes'),
]