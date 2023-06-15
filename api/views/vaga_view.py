from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.vaga_serialize import VagaSerializer
from api.services.vaga_service import listar_vagas


class VagaList(APIView):
    def get(self, request, format=None):
        vagas = listar_vagas()
        serializer = VagaSerializer(vagas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)