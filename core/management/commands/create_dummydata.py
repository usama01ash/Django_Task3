from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from core.models import DateTimeData


class Command(BaseCommand):
    help = 'Creates 100 dummy users and datetime enteries'

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.HTTP_INFO(
            'Creating 100 dummy users with random usernames and passwords'))
        for i in range(100):
            User.objects.create_user(username=get_random_string(
                length=5), password=get_random_string(length=8))

        self.stdout.write(self.style.SUCCESS('100 users added to database'))

        self.stdout.write(self.style.HTTP_INFO(
            'Adding 100 dummy PST datetime objects in database'))
        for i in range(100):
            date_time = DateTimeData()
            date_time.save()

        self.stdout.write(self.style.SUCCESS('100 PST datetime added'))
