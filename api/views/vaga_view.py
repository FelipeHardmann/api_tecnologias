from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import vaga_service
from ..serializers import vaga_serialize


class VagaList(APIView):
    def get(self, request, format=None):
        vagas = vaga_service.listar_vagas()
        serializer = vaga_serialize.VagaSerializer(vagas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)