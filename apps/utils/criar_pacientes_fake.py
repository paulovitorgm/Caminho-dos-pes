import random

from django.utils.text import slugify
from faker import Faker

from apps.pacientes.models import PacientesModel
from apps.utils.barra_de_progresso import barra_de_progresso

fake = Faker('pt_BR')


def criar_email(nome, sobrenome):
    n = random.randint(0, 10000)
    return f'{slugify(nome)}.{slugify(sobrenome)}.{n}@email.com'


def criar_pessoa():
    sexo = random.choice(['m', 'f'])
    nome = fake.first_name()
    sobrenome = fake.last_name()
    return {
        'nome': nome,
        'sobrenome': sobrenome,
        'email': criar_email(nome, sobrenome),
        'sexo': sexo,
        'telefone': fake.numerify('###########'),
        'primeiro_atendimento': fake.date(),
    }


def criar_pacientes(quantidade):
    lista = []
    for _ in barra_de_progresso(range(quantidade), 'Criando pacientes'):
        dados = criar_pessoa()
        objeto = PacientesModel(**dados)
        lista.append(objeto)
    PacientesModel.objects.bulk_create(lista)
