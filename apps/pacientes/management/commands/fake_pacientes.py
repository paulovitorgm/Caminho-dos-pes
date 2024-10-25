from django.core.management import CommandError
from django.core.management.base import BaseCommand

from apps.utils.criar_pacientes_fake import criar_pacientes


class Command(BaseCommand):
    help = 'Criar pacientes'

    def add_arguments(self, parser):  # noqa
        parser.add_argument('--quantidade', '-q', type=int)

    def handle(self, *args, **options):  # noqa
        try:
            qnt = options.get('quantidade') or 100
            criar_pacientes(qnt)
            self.stdout.write(self.style.SUCCESS('Pacientes criados com sucesso.'))
        except CommandError:
            raise CommandError('Pacientes não cadastrados.')
