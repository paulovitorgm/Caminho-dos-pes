from django.core.management import BaseCommand, CommandError

from apps.utils.criar_anamneses_fake import criar_anamnese


class Command(BaseCommand):
    help = 'Criar anamneses'

    def add_arguments(self, parser):  # noqa
        parser.add_argument('--quantidade', '-q', type=int)

    def handle(self, *args, **options):
        try:
            qnt = options.get('quantidade') or 100
            criar_anamnese(qnt)
            self.stdout.write(self.style.SUCCESS('Anamneses criadas com sucesso'))
        except CommandError:
            raise CommandError('Anamneses não cadastradas.')
