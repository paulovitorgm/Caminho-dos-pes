import random

from faker import Faker

from apps.anamnese.models import AnamneseModel
from apps.pacientes.models import PacientesModel
from apps.utils.barra_de_progresso import barra_de_progresso

fake = Faker('pt_BR')


lista_pacientes = PacientesModel.objects.all()


def preencher_anamnese():
    sim_nao = random.choice(['Sim', 'Não'])

    return {
        'paciente': random.choice(lista_pacientes),
        'data': fake.date(),
        'acompanhamento_medico': fake.text(15),
        'medicamento_em_uso': fake.text(15),
        'diabetico': sim_nao,
        'hepatite': sim_nao,
        'hiv': sim_nao,
        'alergia': fake.text(15),
        'teve_cancer': sim_nao,
        'gravidez': sim_nao,
        'lactante': sim_nao,
        'hipertensao': sim_nao,
        'hipotensao': sim_nao,
        'observacoes': fake.text(60),
    }


def criar_anamnese(quantidade):
    lista = []
    for _ in barra_de_progresso(range(quantidade), 'Criando anamneses'):
        dados = preencher_anamnese()
        objeto = AnamneseModel(**dados)
        lista.append(objeto)
    AnamneseModel.objects.bulk_create(lista)
