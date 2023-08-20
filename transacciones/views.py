from django.shortcuts import render
from rest_framework.views import APIView
from .models import Transaccion
from categorias.models import Categoria
from categorias.serializers import CategoriaSerializer
from .serializers import TransaccionSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models.functions import TruncMonth
from django.db.models import Count

# Create your views here.
class Transaccion_api(APIView):
    def get(self, request, format=None):
        transaccion = Transaccion.objects.all()
        serializer = TransaccionSerializer(transaccion, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TransaccionSerializer(data=request.data)
        if serializer.is_valid():
            # Obtenemos la categoría por su ID
            categoria_id = request.data['id_categoria']
            try:
                categoria = Categoria.objects.get(id=categoria_id)
            except Categoria.DoesNotExist:
                return Response({"message": "La categoría especificada no existe"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Incrementamos el atributo 'movimientos', la idea es que cada que realizo una
            # transacción esta se refleje en la categoría
            categoria.movimientos += 1
            categoria.total += request.data['monto']
            categoria.save()
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Mostrar_por_categoria(APIView):
    def get(self, request, categoria_id):
        transaccion = Transaccion.objects.filter(id_categoria=categoria_id)
        serializer = TransaccionSerializer(transaccion, many = True)
        return Response({"data":serializer.data})
    
class Transacciones_por_mes(APIView):
    def get(self, request, categoria_id, format=None,):
        transacciones = Transaccion.objects.filter(id_categoria=categoria_id)

        # Utilizamos annotate y TruncMonth para agrupar las transacciones por mes
        transacciones_por_mes = transacciones.annotate(
            mes=TruncMonth('fecha')
        ).values('mes').annotate(
            total_transacciones=Count('id')
        ).order_by('mes')
        
        # Necesitamos crear una lista para almacenar los resultados
        resultados = []
        cont = 0
        for item in transacciones_por_mes:
            cont += 1
            print(cont)
            mes = item['mes']
            total_transacciones = item['total_transacciones']
            
            # Ahora obtenemos las transacciones para este mes, recodar hay que filtrar por categoría
            transacciones = Transaccion.objects.filter(
                fecha__year=mes.year,
                fecha__month=mes.month,
                id_categoria=categoria_id,
            )
            
            # Serializar las transacciones para este mes
            serializer = TransaccionSerializer(transacciones, many=True)
            
            # Agregar los resultados a la lista
            resultados.append({
                'mes': mes.strftime('%Y-%m'),
                'total_transacciones': total_transacciones,
                'transacciones': serializer.data
            })
        
        return Response(resultados, status=status.HTTP_200_OK)