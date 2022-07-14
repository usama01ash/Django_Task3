from datetime import datetime

import pytz
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class DateTimeData(models.Model):

    date_time = models.DateTimeField()
    Tz = models.CharField(max_length=3)

    def __str__(self):
        return str(self.date_time)


@receiver(pre_save, sender=DateTimeData)
def set_time_date(sender, instance, **kwargs):
    if instance.id is None:
        UTC_datetime = pytz.utc.localize(datetime.utcnow())  # Get UTC datetime
        PST_tz = pytz.timezone('US/Pacific')
        PST_datetime = UTC_datetime.astimezone(
            PST_tz)  # Covert to PST datetime
        instance.date_time = PST_datetime.replace(
            tzinfo=None)  # Make it naive datetime for DB
        instance.Tz = 'PST'

# Model to save informationn that if CronJob should
# covert from PST to UTC or vice versa

class CurrentConversionMode(models.Model):
    # format PST-to-UTC or UTC-to-PST
    current_conv = models.CharField(max_length=10)
