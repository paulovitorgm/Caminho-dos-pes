from datetime import date

from django.test import TestCase

from apps.pacientes.models import PacientesModel
from apps.utils.criar_pacientes_fake import criar_pacientes
from apps.utils.criar_vendas_fake import criar_vendas
from apps.vendas.models import VendasModel


class TestVendasModel(TestCase):
    def setUp(self):
        self.quantidade = 5
        criar_pacientes(self.quantidade)
        self.venda = {
            'data': date.today(),
            'paciente': PacientesModel.objects.first(),
            'servico': 'Parafina',
            'pagamento': 'Pix',
            'total': 90.0,
            'observacoes': 'Teste',
        }

    def test_criar(self):
        VendasModel.objects.create(**self.venda)
        query = VendasModel.objects.filter(**self.venda)
        self.assertTrue(query.exists())
        self.assertEqual(query.first().paciente, self.venda['paciente'])
        self.assertEqual(query.first().total, self.venda['total'])

    def test_listar(self):
        criar_vendas(self.quantidade)
        query = VendasModel.objects.count()
        self.assertEqual(query, self.quantidade)

    def test_update(self):
        criar_vendas(self.quantidade)
        query = VendasModel.objects.get(pk=1)
        for campo, valor in self.venda.items():
            setattr(query, campo, valor)
        query.save()
        self.assertEqual(query.servico, self.venda['servico'])
        self.assertEqual(query.pagamento, self.venda['pagamento'])

    def test_delete_um(self):
        criar_vendas(self.quantidade)
        VendasModel.objects.get(pk=1).delete()
        self.assertEqual(VendasModel.objects.count(), self.quantidade - 1)

    def test_delete_todos(self):
        criar_vendas(self.quantidade)
        VendasModel.objects.all().delete()
        self.assertEqual(VendasModel.objects.count(), 0)
