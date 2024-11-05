from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestAutenticacaoViews(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username='teste',
            password='senhateste',
            first_name='usuario',
            last_name='usuario',
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

    def test_login(self):
        self.client.logout()
        response = self.client.post(
            reverse('autenticacao:login'),
            data={'username': 'teste', 'password': 'senhateste'},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response,
            reverse('autenticacao:detalhar', kwargs={'pk': self.usuario.id}),
        )

    def test_logout(self):
        response = self.client.post(reverse('autenticacao:logout'))
        self.assertRedirects(response, reverse('autenticacao:login'))

    def test_endpoit_lista_usuarios(self):
        response = self.client.get(reverse('autenticacao:listar'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertInHTML('<td>1</td><td>teste</td>', response.content.decode())

    def test_criar_usuario(self):
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

    def test_editar_usuario(self):
        dados = {
            'username': 'testeusuario',
            'first_name': 'teste nome',
            'last_name': 'teste sobrenome',
            'email': 'teste@email.com',
        }
        response = self.client.post(
            reverse('autenticacao:editar', kwargs={'pk': self.usuario.id}),
            data=dados,
        )
        self.assertRedirects(
            response,
            reverse('autenticacao:detalhar', kwargs={'pk': self.usuario.id}),
            HTTPStatus.FOUND,
        )

    def test_deletar_usuario(self):
        response = self.client.post(
            reverse('autenticacao:deletar', kwargs={'pk': self.usuario.id})
        )
        self.assertRedirects(
            response, reverse('autenticacao:criar'), HTTPStatus.FOUND
        )
        self.assertEqual(User.objects.count(), 0)

    def test_detalhar_usuario(self):
        response = self.client.get(
            reverse('autenticacao:detalhar', kwargs={'pk': self.usuario.id})
        )
        self.assertInHTML(
            '<td>1</td><td>usuario usuario</td>', response.content.decode()
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
