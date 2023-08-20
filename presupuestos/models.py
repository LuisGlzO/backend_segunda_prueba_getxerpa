from django.db import models

# Create your models here.
class Presupuestos(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.FloatField()