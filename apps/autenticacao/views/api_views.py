from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from apps.autenticacao.serializers import UserSerializer


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=self.request.user.id)
