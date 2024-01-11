from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Test command"

    def add_arguments(self, parser):
        # Define command line arguments here
        parser.add_argument('arg1', type=str, help='First argument')
        # parser.add_argument('arg2', type=int, help='Second argument')

    def handle(self, *args, **options):
        # Access the arguments using options dictionary
        arg1 = options['arg1']
        # arg2 = options['arg2']

        # Your command logic here
        print(f"Argument 1: {arg1}")
        # print(f"Argument 2: {arg2}")
