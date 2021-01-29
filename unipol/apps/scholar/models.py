
from django.db import models
from django.utils import timezone

from apps.candidates.models import Candidate
from apps.course.models import Course, Subject
# from apps.qualification.models import Subject



class Scholar(models.Model):
    """ Becario """
    # id
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, help_text='Entry candidates scholar')
    courses = models.ManyToManyField(Course, through='ScholarCourse', help_text='Entry courses scholar')
    
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.candidate.curp}'    


class ScholarCourse(models.Model):
    """ Bacarios Curso """
    scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    qualifications = models.ManyToManyField(Subject, through='ScholarCourseSubject')
    status = models.BooleanField(default=False, help_text='Entry status scholar course')

    def __str__(self):
        return f'{self.scholar.candidate.curp} | {self.course.name}'


class ScholarCourseSubject(models.Model):
    """ Evaluación """
    scholarcourse = models.ForeignKey(ScholarCourse, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    evaluation_theoretical = models.IntegerField(default=None)
    evaluation_practice = models.IntegerField(default=None)
    # assistances = models.ForeignKey(Assistance, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} : {self.scholarcourse} : {self.subject}'
    

class Assistance(models.Model):
    """ Asistencia """
    # id
    date = models.DateField(default=timezone.now)
    hour = models.TimeField(default=timezone.now)
    present = models.BooleanField(default=False, help_text='Entry assistence')
    scholar_course_subject = models.ForeignKey(ScholarCourseSubject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} : {self.date} : {self.scholar_course_subject}'