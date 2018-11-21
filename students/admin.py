from django.contrib import admin
from students.models import Record, UserProfileInfo


# Register your models here.

class RecordsAdmin(admin.ModelAdmin):
    list_display = ['batch_code', 'time_pattern',
                    'session', 'program', 'semester',
                    'course', 'course_name', 'planned_start_date',
                    'planned_end_date', 'actual_start_date', 'actual_end_date',
                    'no_of_students', 'planned_sessions', 'actual_sessions', 'attendance', 'faculty']


class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_semester', 'profile_status', 'profile_program']
    list_filter = ['profile_status']


admin.site.register(Record, RecordsAdmin)
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
