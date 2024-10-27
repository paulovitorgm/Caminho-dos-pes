import random

from faker import Faker

from apps.despesas.models import DespesasModel
from apps.utils.barra_de_progresso import barra_de_progresso
from apps.utils.meios_de_pagamento import meio_de_pagamento

fake = Faker('pt_BR')


def preencher_despesa():
    return {
        'data': fake.date(),
        'fornecedor': fake.name(),
        'descricao': fake.text(50),
        'total': fake.pyfloat(3, 2, True),
        'pagamento': random.choice(meio_de_pagamento)[0],
        'observacoes': fake.text(50),
    }


def criar_despesa(quantidade):
    lista = []
    for _ in barra_de_progresso(range(quantidade), 'Despesa'):
        dados = preencher_despesa()
        objeto = DespesasModel(**dados)
        lista.append(objeto)
    DespesasModel.objects.bulk_create(lista)
