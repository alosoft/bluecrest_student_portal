# Generated by Django 2.1.3 on 2018-11-16 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20181116_0316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='image',
            new_name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='city',
        ),
    ]
