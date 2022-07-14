import logging
from datetime import timedelta

from django.core.exceptions import EmptyResultSet

from models import CurrentConversionMode, DateTimeData

logger = logging.getLogger('django')


def datetime_TZ_conversion():

    try:
        conv_mode = CurrentConversionMode.objects.first()
        # if no conversion mode found in db then create entry with initial value PST to UTC
        if conv_mode is None:  
            conv_mode = CurrentConversionMode()
            conv_mode.current_conv = 'PST-to-UTC'
            conv_mode.save()

        conv_to = conv_mode.current_conv[-3:]
        conv_from = conv_mode.current_conv[:3]
        try:
            qs = DateTimeData.objects.filter(Tz=f'{conv_from}')[:5]
            ''' if no record of the requested Time zone then change the conversion mode from
             PST to UTC and vice versa 
             '''
            if not qs.exists():
                conv_to, conv_from = conv_from, conv_to
                conv_mode.current_conv = f'{conv_from}-to-{conv_to}'
                conv_mode.save()
                qs = DateTimeData.objects.filter(Tz=f'{conv_from}')[:5]
            # Timezone convesion
            for obj in qs:
                obj.date_time = TimeZoneConv(obj.date_time, conv_to)
                obj.Tz = conv_to
                obj.save()

        except EmptyResultSet:
            logger.error(
                'The Query for datetime data Resulted in Empty Results')

    except Exception as e:
        logger.error(f'Error getting Coversion Mode: {e}')


def TimeZoneConv(date_time, conv_to_tz):
    ''' This function coverts naive datetime object from UTC tz to PST tz 
    and vice versa
    '''
    if conv_to_tz == 'UTC':
        return date_time + timedelta(hours=7)    # Time difference handling

    elif conv_to_tz == 'PST':
        return date_time - timedelta(hours=7)

    else:
        return None
