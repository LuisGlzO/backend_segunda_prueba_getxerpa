from django.db import models
#from presupuestos.models import Presupuestos

# Create your models here.
class Categoria(models.Model):
    # id_presupuesto = models.ForeignKey(Presupuestos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    limite = models.FloatField()
    total = models.FloatField(default=0.0)
    movimientos = models.PositiveIntegerField(default=0)
