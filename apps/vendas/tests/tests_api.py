from http import HTTPStatus

from django.shortcuts import reverse
from rest_framework.test import APITestCase

from apps.pacientes.models import PacientesModel
from apps.utils.criar_pacientes_fake import criar_pessoa
from apps.vendas.models import VendasModel


class TestAPI(APITestCase):
    def setUp(self):
        self.paciente = PacientesModel.objects.create(**criar_pessoa())
        self.dados = {
            'data': '2024-11-01',
            'paciente': self.paciente,
            'servico': 'Avaliacao',
            'pagamento': 'Pix',
            'total': 100.99,
            'observacoes': '',
        }
        self.vendas = VendasModel.objects.create(**self.dados)
        self.dados['paciente'] = self.paciente.id

    def test_get(self):
        response = self.client.get(reverse('api:vendas-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data['results'][0],
            {
                'id': 1,
                'data': '2024-11-01',
                'paciente': self.paciente.id,
                'servico': 'Avaliacao',
                'pagamento': 'Pix',
                'total': 100.99,
                'observacoes': '',
            }
        )

    def test_post(self):
        response = self.client.post(
            reverse('api:vendas-list'),
            data={
                'data': '2024-11-10',
                'paciente': self.paciente.id,
                'servico': 'Avaliacao',
                'pagamento': 'Pix',
                'total': 100.99,
                'observacoes': 'Avaliação',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(
            response.data,
            {
                'id': 2,
                'data': '2024-11-10',
                'paciente': self.paciente.id,
                'servico': 'Avaliacao',
                'pagamento': 'Pix',
                'total': 100.99,
                'observacoes': 'Avaliação',
            },
        )

    def test_post_data_invalida(self):
        self.dados['data'] = '12/10/2000'
        response = self.client.post(reverse('api:vendas-list'), data=self.dados)
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.data['data'][0],
            'Formato inválido para data. Use um dos formatos a seguir: YYYY-MM-DD.',
        )

    def test_post_paciente_invalido(self):
        self.dados['paciente'] = 5
        response = self.client.post(reverse('api:vendas-list'), data=self.dados)
        self.assertEqual(
            response.data['paciente'][0],
            'Pk inválido "5" - objeto não existe.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_servico_invalido(self):
        self.dados['servico'] = 'teste'
        response = self.client.post(reverse('api:vendas-list'), data=self.dados)
        self.assertEqual(
            response.data['servico'][0],
            '"teste" não é um escolha válido.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_pagamento_invalido(self):
        self.dados['pagamento'] = 'teste'
        response = self.client.post(reverse('api:vendas-list'), data=self.dados)
        self.assertEqual(
            response.data['pagamento'][0], '"teste" não é um escolha válido.'
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_total_invalido_passando_string(self):
        self.dados['total'] = 'teste'
        response = self.client.post(reverse('api:vendas-list'), data=self.dados)
        self.assertEqual(
           response.data['total'][0], 'Um número válido é necessário.'
        )
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
        response = self.client.post(reverse('api:vendas-list'), data=self.dados)
        self.assertEqual(
            response.data['observacoes'][0],
            'Certifique-se de que este campo não tenha mais de 250 caracteres.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_patch(self):
        response = self.client.patch(
            reverse('api:vendas-detail', kwargs={'pk': self.vendas.id}),
            data={'observacoes': 'Paciente elogiou o atendimento.'},
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data,
            {
                'id': 1,
                'paciente': self.paciente.id,
                'data': '2024-11-01',
                'servico': 'Avaliacao',
                'pagamento': 'Pix',
                'total': 100.99,
                'observacoes': 'Paciente elogiou o atendimento.',
            },
        )

    def test_put(self):
        response = self.client.put(
            reverse('api:vendas-detail', kwargs={'pk': self.vendas.id}),
            data={
                'paciente': self.paciente.id,
                'data': '2024-11-01',
                'servico': 'Avaliacao',
                'pagamento': 'Pix',
                'total': 100.99,
                'observacoes': 'Paciente elogiou o atendimento.',
            }
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data,
            {
                'id': 1,
                'paciente': self.paciente.id,
                'data': '2024-11-01',
                'servico': 'Avaliacao',
                'pagamento': 'Pix',
                'total': 100.99,
                'observacoes': 'Paciente elogiou o atendimento.',
            },
        )

    def test_delete(self):
        response = self.client.delete(
            reverse('api:vendas-detail', kwargs={'pk': self.vendas.id})
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(response.data, None)
