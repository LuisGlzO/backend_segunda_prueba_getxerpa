from django.urls import path
from .views import Transaccion_api, Mostrar_por_categoria, Transacciones_por_mes

urlpatterns = [
    path('1.0/transacciones/', Transaccion_api.as_view(), name="transacciones"),
    path('1.0/transacciones/<int:categoria_id>', Mostrar_por_categoria.as_view(), name="transacciones"),
    path('1.0/transacciones/mes/<int:categoria_id>', Transacciones_por_mes.as_view(), name="transacciones_mes"),
    
]