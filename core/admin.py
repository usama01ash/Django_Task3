from django.contrib import admin

from core.models import DateTimeData, CurrentConversionMode

# Register your models here.


@admin.register(DateTimeData)
class DateTimeDataAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'Tz')

@admin.register(CurrentConversionMode)
class ConversionModeAdmin(admin.ModelAdmin):
    list_display = ('current_conv', )

