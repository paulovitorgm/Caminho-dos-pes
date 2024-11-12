from http import HTTPStatus

from django.contrib.auth.models import User
from django.shortcuts import reverse
from rest_framework.test import APITestCase


class TestApiAutenticacao(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(**{
            'username': 'admin',
            'password': 'admin',
            'email': 'admin@admin.com',
        })
        self.client.login(**{'username': 'admin', 'password': 'admin'})

    def test_get(self):
        response = self.client.get(reverse('api:autenticacao-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post(self):
        response = self.client.post(
            reverse('api:autenticacao-list'),
            data={
                'username': 'teste',
                'first_name': 'teste',
                'last_name': 'teste',
                'email': 'teste@teste.com',
                'password': 'teste',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(
            response.data,
            {
                'id': 2,
                'username': 'teste',
                'first_name': 'teste',
                'last_name': 'teste',
                'email': 'teste@teste.com',
            },
        )
        self.assertNotIn('password', response.data)

    def test_put(self):
        response = self.client.put(
            reverse('api:autenticacao-detail', kwargs={'pk': self.usuario.id}),
            data={
                'username': 'teste',
                'first_name': 'teste',
                'last_name': 'teste',
                'email': 'teste@teste.com',
                'password': 'teste',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('username', response.data)
        self.assertIn('first_name', response.data)
        self.assertIn('email', response.data)
        self.assertNotIn('password', response.data)

    def test_path(self):
        response = self.client.patch(
            reverse('api:autenticacao-detail', kwargs={'pk': self.usuario.id}),
            data={'email': 'teste@teste.com', 'last_name': 'teste'},
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('email', response.data)
        self.assertNotIn('password', response.data)
        self.assertEqual(response.data['email'], 'teste@teste.com')
        self.assertEqual(response.data['last_name'], 'teste')

    def test_delete(self):
        response = self.client.delete(
            reverse('api:autenticacao-detail', kwargs={'pk': self.usuario.id})
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(response.data, None)

    def test_get_sem_estar_logado(self):
        self.client.logout()
        response = self.client.get(reverse('api:autenticacao-list'))
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)
        self.assertEqual(
            response.json()['detail'],
            'As credenciais de autenticação não foram fornecidas.',
        )

    def test_post_username_repetido(self):
        response = self.client.post(
            reverse('api:autenticacao-list'),
            data={
                'username': 'admin',
                'first_name': 'teste',
                'last_name': 'teste',
                'password': 'admin',
                'email': 'admin@admin.com',
            },
        )
        self.assertTrue(
            'Este nome de usuário já está em uso.' in response.json()['username']
        )
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_email_repetido(self):
        response = self.client.post(
            reverse('api:autenticacao-list'),
            data={
                'username': 'teste',
                'first_name': 'teste',
                'last_name': 'teste',
                'password': 'admin',
                'email': 'admin@admin.com',
            },
        )
        self.assertTrue('Este email já está em uso.' in response.json()['email'])
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_sem_estar_logado(self):
        self.client.logout()
        response = self.client.post(
            reverse('api:autenticacao-list'),
            data={
                'username': 'teste',
                'first_name': 'teste',
                'last_name': 'teste',
                'email': 'teste@teste.com',
                'password': 'teste',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(
            response.data,
            {
                'id': 2,
                'username': 'teste',
                'first_name': 'teste',
                'last_name': 'teste',
                'email': 'teste@teste.com',
            },
        )
        self.assertNotIn('password', response.data)

    def test_put_sem_estar_logado(self):
        self.client.logout()
        response = self.client.put(
            reverse('api:autenticacao-detail', kwargs={'pk': self.usuario.id}),
            data={
                'username': 'teste',
                'first_name': 'teste',
                'last_name': 'teste',
                'email': 'teste@teste.com',
                'password': 'teste',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)
        self.assertEqual(
            response.json()['detail'],
            'As credenciais de autenticação não foram fornecidas.',
        )

    def test_path_sem_estar_logado(self):
        self.client.logout()
        response = self.client.patch(
            reverse('api:autenticacao-detail', kwargs={'pk': self.usuario.id}),
            data={'email': 'teste@teste.com', 'last_name': 'teste'},
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)
        self.assertEqual(
            response.json()['detail'],
            'As credenciais de autenticação não foram fornecidas.',
        )

    def test_delete_sem_estar_logado(self):
        self.client.logout()
        response = self.client.delete(
            reverse('api:autenticacao-detail', kwargs={'pk': self.usuario.id})
        )
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)
        self.assertEqual(
            response.json()['detail'],
            'As credenciais de autenticação não foram fornecidas.',
        )

        # task m test apps.autenticacao.tests.tests_api
