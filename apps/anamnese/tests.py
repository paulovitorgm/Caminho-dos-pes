from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from apps.anamnese.models import AnamneseModel
from apps.utils.criar_anamneses_fake import criar_anamnese
from apps.utils.criar_pacientes_fake import criar_pacientes


class TestAnamnese(TestCase):
    quantidade = 10
    anamnese = AnamneseModel.objects.first()

    def setUp(self):
        criar_pacientes(self.quantidade)
        criar_anamnese(self.quantidade)

    def test_se_todas_anamneses_foram_criadas(self):
        assert len(AnamneseModel.objects.all()) == self.quantidade

    def test_endpoint_lista_de_anamneses(self):
        response = self.client.get(reverse('anamnese:listar'))
        assert response.status_code == HTTPStatus.OK

    def test_endpoint_detalhes_anamnese(self):
        response = self.client.get(
            reverse('anamnese:detalhar', kwargs={'pk': self.anamnese.pk})
        )
        assert response.status_code == HTTPStatus.OK

    def test_endpoint_delete_anamnese(self):
        response = self.client.get(
            reverse('anamnese:deletar', kwargs={'pk': self.anamnese.pk})
        )
        assert response.status_code == HTTPStatus.OK

    def test_delete_anamnese(self):
        response = self.client.post(
            reverse('anamnese:deletar', kwargs={'pk': self.anamnese.pk})
        )
        assert response.status_code == HTTPStatus.FOUND
        assert not AnamneseModel.objects.filter(pk=self.anamnese.pk).exists()
        self.assertRedirects(response, reverse('anamnese:listar'))

    def test_endpoint_update_anamnese(self):
        response = self.client.get(
            reverse('anamnese:editar', kwargs={'pk': self.anamnese.pk})
        )
        assert response.status_code == HTTPStatus.OK

    # def test_update_anamnese(self): #noqa
    #     nova_anamnese = preencher_anamnese()
    #
    #     response = self.client.post(
    #         reverse('anamnese:editar', kwargs={'pk': self.anamnese.pk}),
    #         data=nova_anamnese,
    #     )
    #
    #     assert response.status_code == HTTPStatus.OK
