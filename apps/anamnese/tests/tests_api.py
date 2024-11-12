from http import HTTPStatus

from django.contrib.auth.models import User
from django.shortcuts import reverse
from rest_framework.test import APITestCase

from apps.anamnese.models import AnamneseModel
from apps.pacientes.models import PacientesModel
from apps.utils.criar_pacientes_fake import criar_pessoa


class TestAPI(APITestCase):
    def setUp(self):
        self.paciente = PacientesModel.objects.create(**criar_pessoa())
        self.dados = {
            'paciente': self.paciente,
            'data': '2024-10-31',
            'acompanhamento_medico': 'Cardiologista',
            'medicamento_em_uso': 'Losartana',
            'diabetico': 'Não',
            'hepatite': 'Não',
            'hiv': 'Não',
            'alergia': 'Amendoim',
            'teve_cancer': 'Sim',
            'gravidez': 'Não',
            'lactante': 'Não',
            'hipertensao': 'Não',
            'hipotensao': 'Não',
            'observacoes': '',
        }
        self.anamnese = AnamneseModel.objects.create(**self.dados)
        self.dados['paciente'] = self.paciente.id
        User.objects.create_superuser(**{
            'username': 'admin',
            'password': 'admin',
            'email': 'admin@admin.com',
        })
        self.client.login(**{'username': 'admin', 'password': 'admin'})

    def test_get(self):
        response = self.client.get(reverse('api:anamneses-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data['results'][0],
            {
                'id': 1,
                'paciente': self.paciente.id,
                'data': '2024-10-31',
                'acompanhamento_medico': 'Cardiologista',
                'medicamento_em_uso': 'Losartana',
                'diabetico': 'Não',
                'hepatite': 'Não',
                'hiv': 'Não',
                'alergia': 'Amendoim',
                'teve_cancer': 'Sim',
                'gravidez': 'Não',
                'lactante': 'Não',
                'hipertensao': 'Não',
                'hipotensao': 'Não',
                'observacoes': '',
            },
        )

    def test_post(self):
        response = self.client.post(
            reverse('api:anamneses-list'),
            data={
                'paciente': self.paciente.id,
                'data': '2024-10-31',
                'acompanhamento_medico': '',
                'medicamento_em_uso': '',
                'diabetico': 'Sim',
                'hepatite': 'Não',
                'hiv': 'Não',
                'alergia': 'Amendoim',
                'teve_cancer': 'Sim',
                'gravidez': 'Não',
                'lactante': 'Não',
                'hipertensao': 'Não',
                'hipotensao': 'Não',
                'observacoes': '',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(
            response.data,
            {
                'id': 2,
                'paciente': self.paciente.id,
                'data': '2024-10-31',
                'acompanhamento_medico': '',
                'medicamento_em_uso': '',
                'diabetico': 'Sim',
                'hepatite': 'Não',
                'hiv': 'Não',
                'alergia': 'Amendoim',
                'teve_cancer': 'Sim',
                'gravidez': 'Não',
                'lactante': 'Não',
                'hipertensao': 'Não',
                'hipotensao': 'Não',
                'observacoes': '',
            },
        )

    def test_post_paciente_invalido(self):
        self.dados['paciente'] = 5
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['paciente'][0],
            'Pk inválido "5" - objeto não existe.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_data_invalida(self):
        self.dados['data'] = '12/10/2000'
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.data['data'][0],
            'Formato inválido para data. Use um dos formatos a seguir: YYYY-MM-DD.',
        )

    def test_post_acompanhamento_medico_invalido(self):
        self.dados['acompanhamento_medico'] = (
            'teste teste teste teste teste '
            'teste teste teste teste teste '
            'teste teste teste teste teste '
        )
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['acompanhamento_medico'][0],
            'Certifique-se de que este campo não tenha mais de 60 caracteres.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_diabetico_invalido(self):
        self.dados['diabetico'] = 'teste'
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['diabetico'][0], '"teste" não é um escolha válido.'
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_hepatite_invalido(self):
        self.dados['hepatite'] = 'teste'
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['hepatite'][0], '"teste" não é um escolha válido.'
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_hiv_invalido(self):
        self.dados['hiv'] = 'teste'
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(response.data['hiv'][0], '"teste" não é um escolha válido.')
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_alergia_invalido(self):
        self.dados['alergia'] = (
            'teste teste teste teste teste '
            'teste teste teste teste teste '
            'teste teste teste teste teste '
        )
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['alergia'][0],
            'Certifique-se de que este campo não tenha mais de 50 caracteres.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_teve_cancer_invalido(self):
        self.dados['teve_cancer'] = 'teste'
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['teve_cancer'][0], '"teste" não é um escolha válido.'
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_gravidez_invalido(self):
        self.dados['gravidez'] = 'teste'
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['gravidez'][0], '"teste" não é um escolha válido.'
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_lactante_invalido(self):
        self.dados['lactante'] = 'teste'
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['lactante'][0], '"teste" não é um escolha válido.'
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_hipertensao_invalido(self):
        self.dados['hipertensao'] = 'teste'
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['hipertensao'][0], '"teste" não é um escolha válido.'
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_post_hipotensao_invalido(self):
        self.dados['hipotensao'] = 'teste'
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['hipotensao'][0], '"teste" não é um escolha válido.'
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
        response = self.client.post(reverse('api:anamneses-list'), data=self.dados)
        self.assertEqual(
            response.data['observacoes'][0],
            'Certifique-se de que este campo não tenha mais de 400 caracteres.',
        )
        self.assertNotEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_patch(self):
        response = self.client.patch(
            reverse('api:anamneses-detail', kwargs={'pk': self.anamnese.id}),
            data={'observacoes': 'Paciente reclamou de dores nos pés'},
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data,
            {
                'id': 1,
                'paciente': self.paciente.id,
                'data': '2024-10-31',
                'acompanhamento_medico': 'Cardiologista',
                'medicamento_em_uso': 'Losartana',
                'diabetico': 'Não',
                'hepatite': 'Não',
                'hiv': 'Não',
                'alergia': 'Amendoim',
                'teve_cancer': 'Sim',
                'gravidez': 'Não',
                'lactante': 'Não',
                'hipertensao': 'Não',
                'hipotensao': 'Não',
                'observacoes': 'Paciente reclamou de dores nos pés',
            },
        )

    def test_put(self):
        response = self.client.put(
            reverse('api:anamneses-detail', kwargs={'pk': self.anamnese.id}),
            data={
                'id': 1,
                'paciente': self.paciente.id,
                'data': '2024-10-31',
                'acompanhamento_medico': 'Cardiologista',
                'medicamento_em_uso': 'Losartana',
                'diabetico': 'Não',
                'hepatite': 'Não',
                'hiv': 'Não',
                'alergia': 'Amendoim',
                'teve_cancer': 'Sim',
                'gravidez': 'Não',
                'lactante': 'Não',
                'hipertensao': 'Não',
                'hipotensao': 'Não',
                'observacoes': 'Paciente reclamou de dores nos pés',
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.data,
            {
                'id': 1,
                'paciente': self.paciente.id,
                'data': '2024-10-31',
                'acompanhamento_medico': 'Cardiologista',
                'medicamento_em_uso': 'Losartana',
                'diabetico': 'Não',
                'hepatite': 'Não',
                'hiv': 'Não',
                'alergia': 'Amendoim',
                'teve_cancer': 'Sim',
                'gravidez': 'Não',
                'lactante': 'Não',
                'hipertensao': 'Não',
                'hipotensao': 'Não',
                'observacoes': 'Paciente reclamou de dores nos pés',
            },
        )

    def test_delete(self):
        response = self.client.delete(
            reverse(
                'api:anamneses-detail',
                kwargs={'pk': self.anamnese.id},
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(response.data, None)
