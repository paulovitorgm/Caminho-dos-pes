from faker import Faker
from faker.providers import DynamicProvider

from apps.anamnese.models import AnamneseModel
from apps.pacientes.models import PacientesModel
from apps.utils.barra_de_progresso import barra_de_progresso

fake = Faker('pt_BR')


lista_pacientes = PacientesModel.objects.all()


def preencher_anamnese():
    sim_nao = DynamicProvider('opcao', ['Sim', 'Não'])
    pacientes = DynamicProvider('paciente', lista_pacientes)
    fake.add_provider(sim_nao)
    fake.add_provider(pacientes)

    return {
        'paciente': fake.paciente(),
        'data': fake.date(),
        'acompanhamento_medico': fake.text(15),
        'medicamento_em_uso': fake.text(15),
        'diabetico': fake.opcao(),
        'hepatite': fake.opcao(),
        'hiv': fake.opcao(),
        'alergia': fake.text(15),
        'teve_cancer': fake.opcao(),
        'gravidez': fake.opcao(),
        'lactante': fake.opcao(),
        'hipertensao': fake.opcao(),
        'hipotensao': fake.opcao(),
        'observacoes': fake.text(60),
    }


def criar_anamnese(quantidade):
    lista = []
    for _ in barra_de_progresso(range(quantidade), 'Criando anamneses'):
        dados = preencher_anamnese()
        objeto = AnamneseModel(**dados)
        lista.append(objeto)
    AnamneseModel.objects.bulk_create(lista)
