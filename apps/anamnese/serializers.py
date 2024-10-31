from rest_framework.serializers import ModelSerializer

from apps.anamnese.models import AnamneseModel


class AnamneseSerializer(ModelSerializer):
    class Meta:
        model = AnamneseModel
        fields = '__all__'
