from django.shortcuts import render
from rest_framework.views import APIView
from .models import Categoria
from transacciones.models import Transaccion
from .serializers import CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Categoria_api(APIView):
    def get(self, request, format=None):
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        #calcular el porcentaje utilizado del presupuesto para cada categoria
        for item in serializer.data:
            if item['limite'] > 0:
                item['porcentaje_usado'] = ( item['total'] / item['limite'] ) * 100
            else:
                item['porcentaje_usado'] = 0
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Categoria_detail(APIView):
    def get(self, request, categoria_id):
        categoria = Categoria.objects.get(id=categoria_id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    def put(self, request, categoria_id):
        categoria = Categoria.objects.get(id=categoria_id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, categoria_id):
        categoria = Categoria.objects.get(id=categoria_id)
        categoria.delete()
        return Response({"message" :" Categoria eliminada"}, status=status.HTTP_200_OK)
