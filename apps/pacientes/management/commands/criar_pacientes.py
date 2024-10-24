from django.core.management.base import BaseCommand
from django.utils.text import slugify

from faker import Faker
from faker.providers import DynamicProvider

from apps.pacientes.models.pacientes import PacientesModel
from apps.utils.barra_de_progresso import barra_de_progresso

fake = Faker('pt_BR')


def criar_email(nome, sobrenome):
    return f'{slugify(nome)}.{slugify(sobrenome)}@email.com'


def criar_pessoa():
    sexo_op = DynamicProvider(
        provider_name='sexo',
        elements=['m', 'f']
    )
    fake.add_provider(sexo_op)
    nome = fake.first_name()
    sobrenome = fake.last_name()
    return {
        'nome': nome,
        'sobrenome': sobrenome,
        'email': criar_email(nome, sobrenome),
        'sexo': fake.sexo(),
        'telefone': fake.numerify('###########'),
        'primeiro_atendimento': fake.date()
    }


def criar_pacientes():
    lista = []
    for _ in barra_de_progresso(range(100), 'Pacientes'):
        dados = criar_pessoa()
        objeto = PacientesModel(**dados)
        lista.append(objeto)
    PacientesModel.objects.bulk_create(lista)


class Command(BaseCommand):
    help = 'Criar pacientes'

    def handle(self, *args, **options):
        criar_pacientes()
