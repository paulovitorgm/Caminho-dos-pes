from datetime import date

from django.test import TestCase

from apps.despesas.models import DespesasModel
from apps.utils.criar_despesas import criar_despesa


class TestDespesasModel(TestCase):
    def setUp(self):
        self.quantidade = 5
        self.despesa = {
            'data': date.today(),
            'fornecedor': 'Potus',
            'descricao': 'Água para autoclave',
            'total': 20.0,
            'pagamento': 'Pix',
            'observacoes': '',
        }

    def test_criar(self):
        DespesasModel.objects.create(**self.despesa)
        query = DespesasModel.objects.filter(**self.despesa)
        self.assertTrue(query.exists())
        self.assertEqual(query.first().fornecedor, self.despesa['fornecedor'])
        self.assertEqual(query.first().total, self.despesa['total'])

    def test_listar(self):
        criar_despesa(self.quantidade)
        query = DespesasModel.objects.count()
        self.assertEqual(query, self.quantidade)

    def test_update(self):
        criar_despesa(self.quantidade)
        query = DespesasModel.objects.get(pk=1)
        for campo, valor in self.despesa.items():
            setattr(query, campo, valor)
        query.save()
        self.assertEqual(query.descricao, self.despesa['descricao'])
        self.assertEqual(query.pagamento, self.despesa['pagamento'])

    def test_delete_um(self):
        criar_despesa(self.quantidade)
        DespesasModel.objects.get(pk=1).delete()
        self.assertEqual(DespesasModel.objects.count(), self.quantidade - 1)

    def test_delete_todos(self):
        criar_despesa(self.quantidade)
        DespesasModel.objects.all().delete()
        self.assertEqual(DespesasModel.objects.count(), 0)
