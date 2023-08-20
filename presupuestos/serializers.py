from rest_framework import serializers
from .models import Presupuestos

class PresupuestosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presupuestos
        fields = '__all__'