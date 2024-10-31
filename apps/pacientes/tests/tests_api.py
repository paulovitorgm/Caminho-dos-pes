from http import HTTPStatus

from django.shortcuts import reverse
from rest_framework.test import APITestCase


class TestAPI(APITestCase):
    dados = {
        'nome': 'José',
        'sobrenome': 'da Silva',
        'email': 'teste@teste.com',
        'sexo': 'M',
        'telefone': '99987654321',
        'primeiro_atendimento': '2024-10-31',
    }

    def test_get(self):
        response = self.client.get(reverse('api:pacientes-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post(self):
        response = self.client.post(reverse('api:pacientes-list'), data=self.dados)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_post_sexo_invalido(self):
        self.dados['sexo'] = 'masculino'
        response = self.client.post(reverse('api:pacientes-list'), data=self.dados)
        self.assertFalse(response.status_code == HTTPStatus.CREATED)
