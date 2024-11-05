from django.contrib.auth.models import User
from django.test import TestCase


class TestAnamneseModel(TestCase):
    def setUp(self):
        User.objects.create(**{'username': 'usuario', 'password': 'senhadeteste'})
        self.dados = {
            'username': 'teste',
            'password': 'senhateste',
            'email': 'teste@teste.com',
            'first_name': 'usuario',
            'last_name': 'usuario',
        }

    def test_criar(self):
        User.objects.create(**self.dados)
        query = User.objects.filter(**self.dados)
        self.assertTrue(query.exists())
        self.assertEqual(query.first().username, self.dados['username'])
        self.assertEqual(query.first().first_name, self.dados['first_name'])

    def test_update(self):
        query = User.objects.get(pk=1)
        for campo, valor in self.dados.items():
            setattr(query, campo, valor)
        query.save()
        self.assertEqual(query.username, self.dados['username'])
        self.assertEqual(query.email, self.dados['email'])

    def test_delete_um(self):
        User.objects.get(pk=1).delete()
        self.assertEqual(User.objects.count(), 0)

    def test_delete_varios(self):
        User.objects.create(**self.dados)
        User.objects.all().delete()
        self.assertEqual(User.objects.count(), 0)
