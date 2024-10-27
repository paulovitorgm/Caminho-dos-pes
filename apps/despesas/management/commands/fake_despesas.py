from django.core.management import BaseCommand, CommandError

from apps.utils.criar_despesas import criar_despesa


class Command(BaseCommand):
    help = 'Criar despesas fake'

    def add_arguments(self, parser):  # noqa
        parser.add_argument('--quantidade', '-q', type=int)

    def handle(self, *args, **options):
        try:
            qnt = options.get('quantidade') or 50
            criar_despesa(qnt)
            self.stdout.write(self.style.SUCCESS('Despesas criadas com sucesso'))
        except CommandError:
            raise CommandError('As despesas não puderam ser criadas.')
