from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

AuthUser = get_user_model()


class Command(BaseCommand):
    help = 'Set a user as superuser and staff'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='The email of the user')

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        try:
            user = AuthUser.objects.get(email=email)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated {email} to superuser and staff status.'))
        except AuthUser.DoesNotExist:
            self.stdout.write(self.style.ERROR('User does not exist.'))
