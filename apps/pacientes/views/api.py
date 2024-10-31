from rest_framework.viewsets import ModelViewSet

from apps.pacientes.models import PacientesModel
from apps.pacientes.serializers import PacientesSerializer


class PacientesViewset(ModelViewSet):
    queryset = PacientesModel.objects.all()
    serializer_class = PacientesSerializer
