from django.contrib import admin
from students import models


# Register your models here.

class RecordsAdmin(admin.ModelAdmin):
    list_display = ['batch_code', 'time_pattern',
                    'session', 'program', 'semester',
                    'course', 'course_name', 'planned_start_date',
                    'planned_end_date', 'actual_start_date', 'actual_end_date',
                    'no_of_students', 'planned_sessions', 'actual_sessions', 'attendance', 'faculty']


admin.site.register(models.Record, RecordsAdmin)
