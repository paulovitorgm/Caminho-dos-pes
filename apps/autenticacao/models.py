from django.contrib.auth.models import User


class UsuarioModel(User):
    def nome_completo(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.username}'

    class Meta:
        proxy = True
