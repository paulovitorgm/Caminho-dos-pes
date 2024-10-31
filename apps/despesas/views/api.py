from rest_framework.viewsets import ModelViewSet

from apps.despesas.models import DespesasModel
from apps.despesas.serializers import DespesasSerializer


class DespesasViewset(ModelViewSet):
    queryset = DespesasModel.objects.all()
    serializer_class = DespesasSerializer
