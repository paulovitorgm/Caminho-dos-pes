from rest_framework.viewsets import ModelViewSet

from apps.vendas.models import VendasModel
from apps.vendas.serializers import VendasSerializer


class VendasViewset(ModelViewSet):
    queryset = VendasModel.objects.all()
    serializer_class = VendasSerializer
