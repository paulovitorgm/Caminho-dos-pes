from rest_framework.serializers import ModelSerializer

from apps.despesas.models import DespesasModel


class DespesasSerializer(ModelSerializer):
    class Meta:
        model = DespesasModel
        fields = '__all__'
