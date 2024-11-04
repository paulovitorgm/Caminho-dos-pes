from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestAutenticacaoViews(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='teste', password='senhateste'
        )
        self.client.login(username='teste', password='senhateste')

    def test_rota_listar_redireciona_usuario_nao_logado(self):
        self.client.logout()
        response = self.client.get(reverse('autenticacao:listar'))
        self.assertRedirects(
            response,
            f'{reverse("autenticacao:login")}?next={reverse("autenticacao:listar")}',
        )

    def test_rota_detalhar_redireciona_usuario_nao_logado(self):
        self.client.logout()
        response = self.client.get(
            reverse('autenticacao:detalhar', kwargs={'pk': 1})
        )
        self.assertRedirects(
            response,
            f'{reverse("autenticacao:login")}?next='
            f'{reverse("autenticacao:detalhar", kwargs={'pk': 1})}',
        )

    def test_rota_editar_redireciona_usuario_nao_logado(self):
        self.client.logout()
        response = self.client.get(reverse('autenticacao:editar', kwargs={'pk': 1}))
        self.assertRedirects(
            response,
            f'{reverse("autenticacao:login")}?next='
            f'{reverse("autenticacao:editar", kwargs={'pk': 1})}',
        )

    def test_rota_deletar_redireciona_usuario_nao_logado(self):
        self.client.logout()
        response = self.client.get(reverse('autenticacao:deletar', kwargs={'pk': 1}))
        self.assertRedirects(
            response,
            f'{reverse("autenticacao:login")}?next='
            f'{reverse("autenticacao:deletar", kwargs={'pk': 1})}',
        )

    def test_logout(self):
        response = self.client.post(reverse('autenticacao:logout'))
        self.assertRedirects(response, reverse('autenticacao:login'))

    def test_endpoit_lista_usuarios(self):
        response = self.client.get(reverse('autenticacao:listar'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertInHTML('<td>1</td><td>teste</td>', response.content.decode())

    def test_endpoint_criar_usuarios(self):
        response = self.client.post(
            reverse('autenticacao:criar'),
            data={
                'username': 'testeusuario',
                'first_name': 'teste nome',
                'last_name': 'teste sobrenome',
                'email': 'teste@email.com',
                'password': 'senhateste',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response.url, reverse('autenticacao:login'))
