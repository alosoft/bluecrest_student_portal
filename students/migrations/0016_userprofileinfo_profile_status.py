# Generated by Django 2.1.3 on 2018-11-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_userprofileinfo_profile_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_status',
            field=models.CharField(choices=[('Lecturer', 'Lecturer'), ('Student', 'Student')], default='Student', max_length=20),
        ),
    ]
