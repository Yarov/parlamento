from parlamento.models import Diputado, Entidad, Partido
from rest_framework import serializers


class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Partido
        fields= ['name', 'image']

class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = ['name']

class DiputadoSerializer(serializers.ModelSerializer):
    entidad = EntidadSerializer()
    partido = PartidoSerializer()
    class Meta:
        model = Diputado
        fields = ['id', 'name', 'distrit', 'entidad', 'partido',
                  'created', 'image', 'email', 'type_lection', 'suplente', 'slug']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
