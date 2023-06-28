from rest_framework.views import APIView
from ..serializers import usuario_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class UsuarioList(APIView):
    permission_classes = [AllowAny]
    # ! O AllowAny funciona para abrir o caminho para o usuário, deixando ele executar os metódos
    # ! Atribuidos a esta classe. 
    def post(self, request, format=None):
        serializer = usuario_serializer.UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)