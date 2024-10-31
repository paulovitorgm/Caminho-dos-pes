from datetime import date

from django.test import TestCase

from apps.pacientes.models import PacientesModel
from apps.utils.criar_pacientes_fake import criar_pacientes


class TestPacientesModel(TestCase):
    def setUp(self):
        self.quantidade = 5
        self.paciente = {
            'nome': 'Pedro',
            'sobrenome': 'da Silva',
            'email': 'email@email.com',
            'sexo': 'm',
            'telefone': '09876543210',
            'primeiro_atendimento': date.today(),
        }

    def test_criar(self):
        PacientesModel.objects.create(**self.paciente)
        query = PacientesModel.objects.filter(**self.paciente)
        self.assertTrue(query.exists())
        self.assertEqual(query.first().nome, self.paciente['nome'])
        self.assertEqual(query.first().telefone, self.paciente['telefone'])

    def test_listar(self):
        criar_pacientes(self.quantidade)
        query = PacientesModel.objects.count()
        self.assertEqual(query, self.quantidade)

    def test_update(self):
        criar_pacientes(self.quantidade)
        query = PacientesModel.objects.get(pk=1)
        for campo, valor in self.paciente.items():
            setattr(query, campo, valor)
        query.save()
        self.assertEqual(query.nome, self.paciente['nome'])
        self.assertEqual(query.telefone, self.paciente['telefone'])

    def test_delete_um(self):
        criar_pacientes(self.quantidade)
        PacientesModel.objects.get(pk=1).delete()
        self.assertEqual(PacientesModel.objects.count(), self.quantidade - 1)

    def test_delete_todos(self):
        criar_pacientes(self.quantidade)
        PacientesModel.objects.all().delete()
        self.assertEqual(PacientesModel.objects.count(), 0)
