from django.db import models
from django.utils.timezone import now

SEXO_OP = [('F', 'Feminino'), ('M', 'Masculino')]


class PacientesModel(models.Model):
    nome = models.CharField(max_length=60, blank=False, null=False)
    sobrenome = models.CharField(max_length=60, blank=False, null=False)
    sexo = models.CharField(choices=SEXO_OP, max_length=1, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    telefone = models.CharField(max_length=11, blank=True, null=True, unique=True)
    primeiro_atendimento = models.DateField(default=now)

    def __str__(self):
        return (
            f'{self.nome} {self.sobrenome}'
            if (self.nome and self.sobrenome)
            else self.nome
        )

    class Meta:
        db_table = 'pacientes'
        verbose_name_plural = 'Pacientes'
