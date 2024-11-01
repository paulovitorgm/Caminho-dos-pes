from django.db import models
from django.utils.timezone import now

from apps.pacientes.models import PacientesModel

SIM_NAO = [('Sim', 'Sim'), ('Não', 'Não')]


class AnamneseModel(models.Model):
    paciente = models.ForeignKey(
        PacientesModel, on_delete=models.CASCADE, related_name='anamnese'
    )

    data = models.DateField(default=now)

    acompanhamento_medico = models.CharField(
        max_length=60, blank=True, default='Não faz'
    )

    medicamento_em_uso = models.CharField(
        max_length=60, blank=True, default='Não faz'
    )

    diabetico = models.CharField(max_length=3, choices=SIM_NAO, default='Não')

    hepatite = models.CharField(max_length=3, choices=SIM_NAO, default='Não')

    hiv = models.CharField(max_length=3, choices=SIM_NAO, default='Não')

    alergia = models.CharField(max_length=50, default='Nenhuma')

    teve_cancer = models.CharField(max_length=3, choices=SIM_NAO, default='Não')

    gravidez = models.CharField(max_length=3, choices=SIM_NAO, default='Não')

    lactante = models.CharField(max_length=3, choices=SIM_NAO, default='Não')

    hipertensao = models.CharField(max_length=3, choices=SIM_NAO, default='Não')

    hipotensao = models.CharField(max_length=3, choices=SIM_NAO, default='Não')

    observacoes = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.paciente.nome

    class Meta:
        db_table = 'anamneses'
        verbose_name_plural = 'Anamneses'
