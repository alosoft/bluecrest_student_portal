# Generated by Django 2.1.3 on 2018-11-21 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_auto_20181121_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='semester',
            field=models.CharField(choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Semester 3', 'Semester 3'), ('Semester 4', 'Semester 4'), ('Semester 5', 'Semester 5'), ('Semester 6', 'Semester 6'), ('Semester 7', 'Semester 7'), ('Semester 8', 'Semester 8')], default='Semester 2', max_length=10),
        ),
    ]
