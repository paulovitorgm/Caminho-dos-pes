import random

from faker import Faker

from apps.pacientes.models import PacientesModel
from apps.utils.barra_de_progresso import barra_de_progresso
from apps.utils.meios_de_pagamento import meio_de_pagamento
from apps.vendas.models import VendasModel, servicos

fake = Faker('pt_BR')

lista_pacientes = PacientesModel.objects.all()


def preencher_dados():
    return {
        'data': fake.date(),
        'paciente': random.choice(lista_pacientes),
        'servico': random.choice(servicos)[0],
        'pagamento': random.choice(meio_de_pagamento)[0],
        'total': fake.pyfloat(3, 2, True),
        'observacoes': fake.text(30),
    }


def criar_vendas(quantidade):
    lista = []
    for _ in barra_de_progresso(range(quantidade), 'Venda'):
        dados = preencher_dados()
        objeto = VendasModel(**dados)
        lista.append(objeto)
    VendasModel.objects.bulk_create(lista)
