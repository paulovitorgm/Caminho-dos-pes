
from django.test import TestCase

from apps.anamnese.models import AnamneseModel
from apps.pacientes.models import PacientesModel
from apps.utils.criar_anamneses_fake import criar_anamnese
from apps.utils.criar_pacientes_fake import criar_pacientes


class TestAnamneseModel(TestCase):
    def setUp(self):
        self.quantidade = 5
        criar_pacientes(self.quantidade)
        paciente = PacientesModel.objects.get(pk=1)
        self.anamnese = {
            "paciente": paciente,
            "data": "2002-02-07",
            "acompanhamento_medico": "Possimus ab.",
            "medicamento_em_uso": "Corrupti alias.",
            "diabetico": "Sim",
            "hepatite": "Sim",
            "hiv": "Sim",
            "alergia": "Illum.",
            "teve_cancer": "Sim",
            "gravidez": "Sim",
            "lactante": "Sim",
            "hipertensao": "Sim",
            "hipotensao": "Sim",
            "observacoes": "Quasi et ipsa. Id vel fuga tempora animi."
        }

    def test_criar(self):
        AnamneseModel.objects.create(**self.anamnese)
        query = AnamneseModel.objects.filter(**self.anamnese)
        self.assertTrue(query.exists())
        self.assertEqual(query.first().paciente, self.anamnese['paciente'])
        self.assertEqual(query.first().observacoes, self.anamnese['observacoes'])

    def test_listar(self):
        criar_anamnese(self.quantidade)
        query = AnamneseModel.objects.all()
        self.assertEqual(len(query), self.quantidade)

    def test_update(self):
        criar_anamnese(self.quantidade)
        query = AnamneseModel.objects.get(pk=1)
        for campo, valor in self.anamnese.items():
            setattr(query, campo, valor)
        query.save()
        self.assertEqual(query.paciente, self.anamnese['paciente'])
        self.assertEqual(query.observacoes, self.anamnese['observacoes'])

    def test_delete_um(self):
        criar_anamnese(self.quantidade)
        AnamneseModel.objects.get(pk=1).delete()
        self.assertEqual(len(AnamneseModel.objects.all()),
                         self.quantidade - 1)

    def test_delete_todos(self):
        criar_anamnese(self.quantidade)
        AnamneseModel.objects.all().delete()
        self.assertEqual(len(AnamneseModel.objects.all()), 0)
