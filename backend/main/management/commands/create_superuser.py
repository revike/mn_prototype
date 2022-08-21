from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Команда для создания супер юзера"""

    def handle(self, *args, **options):
        if not User.objects.filter(is_staff=True, is_superuser=True):
            admins = ['admin', 'admin1']
            for admin in admins:
                User.objects.create_superuser(
                    username=admin, password=admin,
                    last_name=admin, first_name=admin
                )
