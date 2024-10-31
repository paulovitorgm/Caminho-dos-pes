from rest_framework.serializers import ModelSerializer

from apps.vendas.models import VendasModel


class VendasSerializer(ModelSerializer):
    class Meta:
        model = VendasModel
        fields = '__all__'
