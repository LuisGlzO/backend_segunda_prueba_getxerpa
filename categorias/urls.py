from django.urls import path
from .views import Categoria_api, Categoria_detail

urlpatterns = [
    path('1.0/categorias/', Categoria_api.as_view(), name="categorias"),
    path('1.0/categorias/<int:categoria_id>', Categoria_detail.as_view(), name="categorias")
]