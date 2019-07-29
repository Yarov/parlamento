from parlamento.models import Diputado, Entidad
from rest_framework import serializers


class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = ['name']

class DiputadoSerializer(serializers.ModelSerializer):
    entidad = EntidadSerializer()
    class Meta:
        model = Diputado
        fields = ['id', 'name', 'distrit', 'entidad', 'partido',
                  'created', 'image', 'email', 'type_lection', 'suplente', 'entidad']
