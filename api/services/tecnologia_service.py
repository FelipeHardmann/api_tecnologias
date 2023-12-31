from ..models import Tecnologia
from django.http import Http404

def listar_tecnologias():
    tecnologias = Tecnologia.objects.all()
    return tecnologias

def cadastrar_tecnologia(tecnologia):
    return Tecnologia.objects.create(nome=tecnologia.nome)

def listar_tecnologia_id(id):
    try:
        return Tecnologia.objects.get(id=id)
    except Tecnologia.DoesNotExist:
        raise Http404
    
def editar_tecnologia(tecnologia_antiga, tecnologia_nova):
    tecnologia_antiga.nome = tecnologia_nova.nome
    tecnologia_antiga.save(force_update=True)

def remover_tecnologia(tecnologia):
    tecnologia.delete()