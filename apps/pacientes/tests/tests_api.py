from http import HTTPStatus

from django.contrib.auth.models import User
from django.shortcuts import reverse
from rest_framework.test import APITestCase

from apps.pacientes.models import PacientesModel


class TestAPI(APITestCase):
    def setUp(self):
        self.dados = {
            'nome': 'José',
            'sobrenome': 'da Silva',
            'email': 'teste@teste.com',
            'sexo': 'M',
            'telefone': '99987654321',
            'primeiro_atendimento': '2024-10-31',
        }
        self.paciente = PacientesModel.objects.create(**self.dados)
        User.objects.create_superuser(**{
            'username': 'admin',
            'password': 'admin',
            'email': 'admin@admin.com',
        })
        self.client.login(**{'username': 'admin', 'password': 'admin'})

    def test_get(self):
        response = self.client.get(reverse('api:pacientes-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data['results'][0],
            {
                'id': 1,
                'nome': 'José',
                'sobrenome': 'da Silva',
                'sexo': 'M',
                'email': 'teste@teste.com',
                'telefone': '99987654321',
                'primeiro_atendimento': '2024-10-31',
            },
        )

    def test_post(self):
        response = self.client.post(
            reverse('api:pacientes-list'),
            data={
                'nome': 'Maria',
                'sobrenome': 'José',
                'email': 'test@test.com',
                'sexo': 'F',
                'telefone': '12345612311',
                'primeiro_atendimento': '2024-10-31',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(
            response.data,
            {
                'id': 2,
                'nome': 'Maria',
                'sobrenome': 'José',
                'email': 'test@test.com',
                'sexo': 'F',
                'telefone': '12345612311',
                'primeiro_atendimento': '2024-10-31',
            },
        )

    def test_post_nome_invalido(self):
        self.dados['nome'] = (
            'teste teste teste teste '
            'teste teste teste teste teste '
            'teste teste teste teste teste teste '
        )
        response = self.client.post(reverse('api:pacientes-list'), data=self.dados)
        self.assertEqual(
            response.data['nome'][0],
            'Certifique-se de que este campo não tenha mais de 60 caracteres.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_sobrenome_invalido(self):
        self.dados['sobrenome'] = (
            'teste teste teste teste '
            'teste teste teste teste teste '
            'teste teste teste teste teste teste '
        )
        response = self.client.post(reverse('api:pacientes-list'), data=self.dados)
        self.assertEqual(
            response.data['sobrenome'][0],
            'Certifique-se de que este campo não tenha mais de 60 caracteres.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_email_invalido(self):
        self.dados['email'] = 'testetesteteste'
        response = self.client.post(reverse('api:pacientes-list'), data=self.dados)
        self.assertEqual(
            response.data['email'][0], 'Insira um endereço de email válido.'
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_sexo_invalido(self):
        self.dados['sexo'] = 'masculino'
        response = self.client.post(reverse('api:pacientes-list'), data=self.dados)
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.data['sexo'][0], '"masculino" não é um escolha válido.'
        )

    def test_post_telefone_invalido(self):
        self.dados['telefone'] = '98765432100000'
        response = self.client.post(reverse('api:pacientes-list'), data=self.dados)
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.data['telefone'][0],
            'Certifique-se de que este campo não tenha mais de 11 caracteres.',
        )

    def test_post_data_invalida(self):
        self.dados['primeiro_atendimento'] = '12/10/2000'
        response = self.client.post(reverse('api:pacientes-list'), data=self.dados)

        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.data['primeiro_atendimento'][0],
            'Formato inválido para data. Use um dos formatos a seguir: YYYY-MM-DD.',
        )

    def test_patch(self):
        response = self.client.patch(
            reverse('api:pacientes-detail', kwargs={'pk': self.paciente.id}),
            data={'nome': 'João'},
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data,
            {
                'id': 1,
                'nome': 'João',
                'sobrenome': 'da Silva',
                'sexo': 'M',
                'email': 'teste@teste.com',
                'telefone': '99987654321',
                'primeiro_atendimento': '2024-10-31',
            },
        )

    def test_put(self):
        response = self.client.put(
            reverse('api:pacientes-detail', kwargs={'pk': self.paciente.id}),
            data={
                'nome': 'Maria',
                'sobrenome': 'da Graça',
                'sexo': 'F',
                'email': 'teste@teste.com',
                'telefone': '12345678900',
                'primeiro_atendimento': '2024-01-10',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data,
            {
                'id': 1,
                'nome': 'Maria',
                'sobrenome': 'da Graça',
                'sexo': 'F',
                'email': 'teste@teste.com',
                'telefone': '12345678900',
                'primeiro_atendimento': '2024-01-10',
            },
        )

    def test_delete(self):
        response = self.client.delete(
            reverse('api:pacientes-detail', kwargs={'pk': self.paciente.id})
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(response.data, None)
