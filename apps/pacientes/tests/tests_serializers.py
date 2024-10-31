from django.test import TestCase

from apps.pacientes.models import PacientesModel
from apps.pacientes.serializers import PacientesSerializer


class TestPacienteSerializer(TestCase):
    def setUp(self):
        self.paciente = PacientesModel.objects.create(
            nome='José',
            sobrenome='da Silva',
            email='teste@teste.com',
            sexo='M',
            telefone='99987654321',
            primeiro_atendimento='2024-10-31',
        )
        self.paciente_serializer = PacientesSerializer(instance=self.paciente)

    def test_verifica_campos_serializados(self):
        dados = self.paciente_serializer.fields.keys()
        self.assertEqual(
            dados,
            {
                'id',
                'nome',
                'sobrenome',
                'email',
                'sexo',
                'telefone',
                'primeiro_atendimento',
            },
        )

    def test_verifica_valores_serializados(self):
        dados = self.paciente_serializer.data
        esperado = {
            'id': 1,
            'nome': 'José',
            'sobrenome': 'da Silva',
            'email': 'teste@teste.com',
            'sexo': 'M',
            'telefone': '99987654321',
            'primeiro_atendimento': '2024-10-31',
        }
        for chave, valor in dados.items():
            self.assertEqual(valor, esperado[chave])
