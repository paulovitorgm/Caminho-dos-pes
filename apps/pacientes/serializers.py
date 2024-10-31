from rest_framework.serializers import ModelSerializer

from apps.pacientes.models import PacientesModel


class PacientesSerializer(ModelSerializer):
    class Meta:
        model = PacientesModel
        fields = '__all__'
