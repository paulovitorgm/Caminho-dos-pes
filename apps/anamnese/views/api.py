from rest_framework.viewsets import ModelViewSet

from apps.anamnese.models import AnamneseModel
from apps.anamnese.serializers import AnamneseSerializer


class AnamnesesViewset(ModelViewSet):
    queryset = AnamneseModel.objects.all()
    serializer_class = AnamneseSerializer
