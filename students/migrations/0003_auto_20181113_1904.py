# Generated by Django 2.1.3 on 2018-11-13 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20181113_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='actual_end',
            new_name='actual_end_date',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='actual_start',
            new_name='actual_start_date',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='student_roll',
            new_name='no_of_students',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='planned_end',
            new_name='planned_end_date',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='planned_start',
            new_name='planned_start_date',
        ),
    ]
