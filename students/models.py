from django.db import models
from django.contrib.auth.models import User


# Create your database models here.
class UserProfileInfo(models.Model):
    status = (
        ('Lecturer', 'Lecturer'),
        ('Student', 'Student')
    )
    BBA = 'BBA'
    BScIT1 = 'BScIT1'
    BScIT = 'BScIT'
    PCHN = 'PCHN'
    PCCA = 'PCCA'
    BAMJ = 'BAMJ'
    Semester1 = 'Semester 1'
    Semester2 = 'Semester 2'
    Semester3 = 'Semester 3'
    Semester4 = 'Semester 4'
    Semester5 = 'Semester 5'
    Semester6 = 'Semester 6'
    Semester7 = 'Semester 7'
    Semester8 = 'Semester 8'

    program_choice = (
        (BBA, 'BBA'),
        (BScIT, 'BScIT'),
        (BScIT1, 'BScIT1'),
        (PCHN, 'PCHN'),
        (PCCA, 'PCCA'),
        (BAMJ, 'BAMJ'),
    )

    semester_choice = (
        (Semester1, 'Semester 1'),
        (Semester2, 'Semester 2'),
        (Semester3, 'Semester 3'),
        (Semester4, 'Semester 4'),
        (Semester5, 'Semester 5'),
        (Semester6, 'Semester 6'),
        (Semester7, 'Semester 7'),
        (Semester8, 'Semester 8')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    profile_semester = models.CharField(max_length=20, blank=True, default='Semester 2', choices=semester_choice)
    profile_program = models.CharField(max_length=20, blank=True, default='Semester 2', choices=program_choice)
    profile_status = models.CharField(default='Student', choices=status, max_length=20)

    def __str__(self):
        return self.user.username


class Record(models.Model):
    BBA = 'BBA'
    BScIT1 = 'BScIT1'
    BScIT = 'BScIT'
    PCHN = 'PCHN'
    PCCA = 'PCCA'
    BAMJ = 'BAMJ'
    Semester1 = 'Semester 1'
    Semester2 = 'Semester 2'
    Semester3 = 'Semester 3'
    Semester4 = 'Semester 4'
    Semester5 = 'Semester 5'
    Semester6 = 'Semester 6'
    Semester7 = 'Semester 7'
    Semester8 = 'Semester 8'

    program_choice = (
        (BBA, 'BBA'),
        (BScIT, 'BScIT'),
        (BScIT1, 'BScIT1'),
        (PCHN, 'PCHN'),
        (PCCA, 'PCCA'),
        (BAMJ, 'BAMJ'),
    )

    semester_choice = (
        (Semester1, 'Semester 1'),
        (Semester2, 'Semester 2'),
        (Semester3, 'Semester 3'),
        (Semester4, 'Semester 4'),
        (Semester5, 'Semester 5'),
        (Semester6, 'Semester 6'),
        (Semester7, 'Semester 7'),
        (Semester8, 'Semester 8')
    )

    batch_code = models.CharField(max_length=20)
    time_pattern = models.CharField(max_length=50)
    session = models.CharField(max_length=20)
    program = models.CharField(max_length=10, choices=program_choice)
    semester = models.CharField(max_length=10, choices=semester_choice, default='Semester 2')
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
