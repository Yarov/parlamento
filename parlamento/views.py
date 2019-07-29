from rest_framework import viewsets, filters
from parlamento.models import Diputado
from parlamento.serializers import DiputadoSerializer


class DipudatoView(viewsets.ModelViewSet):
    queryset = Diputado.objects.all()
    serializer_class = DiputadoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']
    filterset_fields = ['partido']
