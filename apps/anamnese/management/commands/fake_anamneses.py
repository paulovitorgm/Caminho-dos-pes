# SIM_NAO = [('s', 'Sim'), ('n', 'Não')]
# paciente = models.OneToOneField(
#         PacientesModel, on_delete=models.CASCADE, related_name='anamnese'
#     )
#
#     acompanhamento_medico = models.CharField(
#         max_length=100, blank=True, default='Não faz'
#     )
#
#     medicamento_em_uso = models.CharField(
#         max_length=200, blank=True, default='Não faz'
#     )
#
#     diabetico = models.CharField(max_length=1, choices=SIM_NAO, default='n')
#
#     hepatite = models.CharField(max_length=1, choices=SIM_NAO, default='n')
#
#     hiv = models.CharField(max_length=1, choices=SIM_NAO, default='n')
#
#     alergico = models.CharField(max_length=50, default='Nenhuma')
#
#     teve_cancer = models.CharField(max_length=1, choices=SIM_NAO, default='n')
#
#     gravidez = models.CharField(max_length=1, choices=SIM_NAO, default='n')
#
#     lactante = models.CharField(max_length=1, choices=SIM_NAO, default='n')
#
#     hipertensao = models.CharField(max_length=1, choices=SIM_NAO, default='n')
#
#     hipotensao = models.CharField(max_length=1, choices=SIM_NAO, default='n')
#
#     observacoes = models.TextField(max_length=400, blank=True)

from django.core.management import BaseCommand
from faker import Faker

fake = Faker('pt_BR')


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Chamada')
