from django.contrib import admin
from .models import TimeTable


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'section', 'subject', 'teacher',
                    'day', 'start_time', 'end_time')
    search_fields = ('class_name', 'section', 'subject__name')
    list_filter = ('day', 'class_name')
