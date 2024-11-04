from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from apps.anamnese.models import AnamneseModel
from apps.utils.criar_anamneses_fake import criar_anamnese
from apps.utils.criar_pacientes_fake import criar_pacientes


class TestViewsAnamnese(TestCase):
    quantidade = 10
    chave_primaria = 1

    def setUp(self):
        criar_pacientes(self.quantidade)
        criar_anamnese(self.quantidade)

    def test_endpoints_lista_de_anamneses(self):
        response = self.client.get(reverse('anamnese:listar'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_endpoint_detalhes_anamnese(self):
        response = self.client.get(
            reverse('anamnese:detalhar', kwargs={'pk': self.chave_primaria})
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_endpoint_delete_anamnese(self):
        response = self.client.get(
            reverse('anamnese:deletar', kwargs={'pk': self.chave_primaria})
        )
        assert response.status_code == HTTPStatus.OK

    def test_delete_anamnese(self):
        response = self.client.post(
            reverse('anamnese:deletar', kwargs={'pk': self.chave_primaria})
        )
        assert response.status_code == HTTPStatus.FOUND
        assert not AnamneseModel.objects.filter(pk=self.chave_primaria).exists()
        self.assertRedirects(response, reverse('anamnese:listar'))

    def test_endpoint_update_anamnese(self):
        response = self.client.get(
            reverse('anamnese:editar', kwargs={'pk': self.chave_primaria})
        )
        assert response.status_code == HTTPStatus.OK

    def test_endpoint_create(self):
        response = self.client.get(reverse('anamnese:criar'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
