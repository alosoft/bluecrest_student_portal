# Generated by Django 2.1.3 on 2018-11-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_auto_20181121_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_program',
            field=models.CharField(blank=True, choices=[('BBA', 'BBA'), ('BScIT', 'BScIT'), ('BScIT1', 'BScIT1'), ('PCHN', 'PCHN'), ('PCCA', 'PCCA'), ('BAMJ', 'BAMJ')], default='Semester 2', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_semester',
            field=models.CharField(blank=True, choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Semester 3', 'Semester 3'), ('Semester 4', 'Semester 4'), ('Semester 5', 'Semester 5'), ('Semester 6', 'Semester 6'), ('Semester 7', 'Semester 7'), ('Semester 8', 'Semester 8')], default='Semester 2', max_length=20),
        ),
    ]