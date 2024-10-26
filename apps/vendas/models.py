from django.db import models
from django.utils.timezone import now

from apps.pacientes.models import PacientesModel
from apps.utils.meios_de_pagamento import meio_de_pagamento

servicos = [
    ('Avaliacao', 'Avaliação'),
    ('Assepsia completa', 'Assepsia completa'),
    ('Assepsia plantar', 'Assepsia plantar ou laminar'),
    ('Ortese', 'Órtese'),
    ('Curativo', 'Curativo'),
    ('Parafina', 'Hidratação com parafina'),
    ('Unha enc', 'Unha encravada'),
    ('Corte', 'Corte anatômico'),
    ('Calo', 'Calo'),
    ('Laser', 'Laser'),
    ('Outros', 'Outros'),
]


class VendasModel(models.Model):
    data = models.DateField(default=now)
    paciente = models.ForeignKey(PacientesModel, on_delete=models.CASCADE)
    servico = models.CharField(max_length=30, choices=servicos)
    pagamento = models.TextField(max_length=20, choices=meio_de_pagamento)
    total = models.FloatField()
    observacoes = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.servico

    class Meta:
        db_table = 'vendas'
        verbose_name_plural = 'Vendas'
