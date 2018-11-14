from django.db import models


# Create your database models here.
class Record(models.Model):

    BBA = 'BBA'
    BScIT1 = 'BScIT1'
    BScIT = 'BScIT'
    PCHN = 'PCHN'
    PCCA = 'PCCA'
    BAMJ = 'BAMJ'
    BBA = 'BBA'
    sem1 = 'sem1'
    sem2 = 'sem2'
    sem3 = 'sem3'
    sem4 = 'sem4'
    sem5 = 'sem5'
    sem6 = 'sem6'
    sem7 = 'sem7'
    sem8 = 'sem8'

    program_choice = (
        (BBA, 'BBA'),
        (BScIT, 'BScIT'),
        (BScIT1, 'BScIT1'),
        (PCHN, 'PCHN'),
        (PCCA, 'PCCA'),
        (BAMJ, 'BAMJ'),
        (BBA, 'BBA')
    )

    semester_choice = (
        (sem1, 'sem1'),
        (sem2, 'sem2'),
        (sem3, 'sem3'),
        (sem4, 'sem4'),
        (sem5, 'sem5'),
        (sem6, 'sem6'),
        (sem7, 'sem7'),
        (sem8, 'sem8')
    )

    batch_code = models.CharField(max_length=20)
    time_pattern = models.CharField(max_length=50)
    session = models.CharField(max_length=20)
    program = models.CharField(max_length=10, choices=program_choice)
    semester = models.CharField(max_length=10, choices=semester_choice)
    course = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    planned_start_date = models.DateField()
    planned_end_date = models.DateField()
    actual_start_date = models.DateField(blank=True, null=True)
    actual_end_date = models.DateField(blank=True, null=True)
    no_of_students = models.IntegerField()
    planned_sessions = models.IntegerField()
    actual_sessions = models.IntegerField()
    attendance = models.FloatField(blank=True, null=True)
    faculty = models.CharField(max_length=50)

    class Meta:
        ordering = ['time_pattern']

    def __str__(self):
        return self.course_name