# Generated by Django 2.1.3 on 2018-11-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_auto_20181120_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_program',
            field=models.CharField(default='BScIT1', max_length=20),
            preserve_default=False,
        ),
    ]
