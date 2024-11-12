from http import HTTPStatus

from django.contrib.auth.models import User
from django.shortcuts import reverse
from rest_framework.test import APITestCase

from apps.despesas.models import DespesasModel


class TestAPI(APITestCase):
    def setUp(self):
        self.dados = {
            'data': '2024-11-01',
            'fornecedor': 'Teste',
            'descricao': 'Test',
            'total': 123.45,
            'pagamento': 'Pix',
            'observacoes': '',
        }
        self.despesas = DespesasModel.objects.create(**self.dados)
        User.objects.create_superuser(**{
            'username': 'admin',
            'password': 'admin',
            'email': 'admin@admin.com',
        })
        self.client.login(**{'username': 'admin', 'password': 'admin'})

    def test_get(self):
        response = self.client.get(reverse('api:despesas-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data['results'][0],
            {
                'id': 1,
                'data': '2024-11-01',
                'fornecedor': 'Teste',
                'descricao': 'Test',
                'total': 123.45,
                'pagamento': 'Pix',
                'observacoes': '',
            },
        )

    def test_post(self):
        response = self.client.post(
            reverse('api:despesas-list'),
            data=self.dados,
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(
            response.data,
            {
                'id': 2,
                'data': '2024-11-01',
                'fornecedor': 'Teste',
                'descricao': 'Test',
                'total': 123.45,
                'pagamento': 'Pix',
                'observacoes': '',
            },
        )

    def test_post_data_invalida(self):
        self.dados['data'] = '12/10/2000'
        response = self.client.post(reverse('api:despesas-list'), data=self.dados)
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.data['data'][0],
            'Formato inválido para data. Use um dos formatos a seguir: YYYY-MM-DD.',
        )

    def test_post_fornecedor_invalido(self):
        self.dados['fornecedor'] = (
            'teste teste teste teste teste '
            'teste teste teste teste teste '
            'teste teste teste teste teste '
        )
        response = self.client.post(reverse('api:despesas-list'), data=self.dados)
        print(response.data)
        self.assertEqual(
            response.data['fornecedor'][0],
            'Certifique-se de que este campo não tenha mais de 50 caracteres.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_descricao_invalido(self):
        self.dados['descricao'] = (
            'Django é um framework web em Python amplamente utilizado '
            'para desenvolvimento de aplicações robustas e escaláveis. '
            'Criado para simplificar tarefas comuns no desenvolvimento web, '
            'ele oferece ferramentas para autenticação, gerenciamento de sessões, '
            'formulários e segurança, permitindo que os desenvolvedores foquem na '
            'lógica de negócio. Com uma estrutura modular, Django é ideal '
            'para sites de todos os portes, de blogs a aplicações empresariais'
            ' complexas, tornando o desenvolvimento mais rápido e seguro.'
        )
        response = self.client.post(reverse('api:despesas-list'), data=self.dados)
        self.assertEqual(
            response.data['descricao'][0],
            'Certifique-se de que este campo não tenha mais de 200 caracteres.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_pagamento_invalido(self):
        self.dados['pagamento'] = 'teste'
        response = self.client.post(reverse('api:despesas-list'), data=self.dados)
        self.assertEqual(
            response.data['pagamento'][0], '"teste" não é um escolha válido.'
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_total_invalido_passando_string(self):
        self.dados['total'] = 'teste'
        response = self.client.post(reverse('api:despesas-list'), data=self.dados)
        self.assertEqual(response.data['total'][0], 'Um número válido é necessário.')
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_observacoes_invalido(self):
        self.dados['observacoes'] = (
            'Django é um framework web em Python amplamente utilizado '
            'para desenvolvimento de aplicações robustas e escaláveis. '
            'Criado para simplificar tarefas comuns no desenvolvimento web, '
            'ele oferece ferramentas para autenticação, gerenciamento de sessões, '
            'formulários e segurança, permitindo que os desenvolvedores foquem na '
            'lógica de negócio. Com uma estrutura modular, Django é ideal '
            'para sites de todos os portes, de blogs a aplicações empresariais'
            ' complexas, tornando o desenvolvimento mais rápido e seguro.'
        )
        response = self.client.post(reverse('api:despesas-list'), data=self.dados)
        self.assertEqual(
            response.data['observacoes'][0],
            'Certifique-se de que este campo não tenha mais de 200 caracteres.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_patch(self):
        response = self.client.patch(
            reverse('api:despesas-detail', kwargs={'pk': self.despesas.id}),
            data={'observacoes': 'Produto veio aberto.'},
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data,
            {
                'id': self.despesas.id,
                'data': '2024-11-01',
                'fornecedor': 'Teste',
                'descricao': 'Test',
                'total': 123.45,
                'pagamento': 'Pix',
                'observacoes': 'Produto veio aberto.',
            },
        )

    def test_put(self):
        response = self.client.put(
            reverse('api:despesas-detail', kwargs={'pk': self.despesas.id}),
            data={
                'data': '2024-11-01',
                'fornecedor': 'Teste',
                'descricao': 'Test',
                'total': 123.45,
                'pagamento': 'Pix',
                'observacoes': '',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data,
            {
                'id': self.despesas.id,
                'data': '2024-11-01',
                'fornecedor': 'Teste',
                'descricao': 'Test',
                'total': 123.45,
                'pagamento': 'Pix',
                'observacoes': '',
            },
        )

    def test_delete(self):
        response = self.client.delete(
            reverse('api:despesas-detail', kwargs={'pk': self.despesas.id})
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(response.data, None)
