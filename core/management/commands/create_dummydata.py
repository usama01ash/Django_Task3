from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Creates 100 dummy users and datetime enteries'

    def handle(self, *args, **kwargs):
        for i in range(100):
            User.objects.create_user(username=get_random_string(
                length=5), password=get_random_string(length=8))
