from django.db import models
from categorias.models import Categoria

# Create your models here.
class Transaccion(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    monto = models.FloatField()
    fecha = models.DateTimeField()
    ignorar = models.BooleanField(default=False)