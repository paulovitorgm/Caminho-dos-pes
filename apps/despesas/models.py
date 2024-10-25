from django.db import models
from django.utils.timezone import now
from apps.utils.meios_de_pagamento import meio_de_pagamento


class DespesasModel(models.Model):
    data = models.DateField(default=now)
    fornecedor = models.CharField(max_length=50,)
    descricao = models.CharField(max_length=200)
    total = models.FloatField()
    pagamento = models.CharField(max_length=20, choices=meio_de_pagamento)
    observacoes = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.descricao[:25]

    class Meta:
        db_table = 'despesas'
        verbose_name_plural = 'Despesas'
