from django.core.management import BaseCommand, CommandError

from apps.utils.criar_vendas_fake import criar_vendas


class Command(BaseCommand):
    help = 'Criar vendas fake'

    def add_arguments(self, parser):  # noqa
        parser.add_argument('--quantidade', '-q', type=int)

    def handle(self, *args, **options):
        try:
            qnt = options.get('quantidade') or 50
            criar_vendas(qnt)
            self.stdout.write(self.style.SUCCESS('Vendas criadas com sucesso'))
        except CommandError:
            raise CommandError('As vendas não puderam ser criadas.')
