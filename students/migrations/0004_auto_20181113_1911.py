# Generated by Django 2.1.3 on 2018-11-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20181113_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='attendance',
            field=models.FloatField(blank=True),
        ),
    ]
