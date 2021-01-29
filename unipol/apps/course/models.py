from datetime import date
from django.db import models
from django.utils import timezone



    


class Zone(models.Model):
    """ Zona """
    # id zona
    name = models.CharField(max_length=50, help_text='Entry name zone')

    def __str__(self):
        return f'{self.id} | {self.name}'


class Campus(models.Model):
    """ Sede """
    # id
    
    zone = models.OneToOneField(Zone, on_delete=models.CASCADE, help_text='Entry zone campus')
    name = models.CharField(max_length=255, help_text='Entry name campus') 
    status = models.BooleanField(default=True, help_text='Entry status campus')
    capacity = models.IntegerField(default=700, help_text='Entry capacity campu')
    direction = models.CharField(max_length=255, help_text='Entry direction campus')
    
    def __str__(self):
        return f'{self.id} : {self.name}'
    
    

class Course(models.Model):
    """ Curso """
    # id course
    name = models.CharField(max_length=255, help_text='Entry name course')
    status = models.BooleanField(default=False, help_text='Entry status course')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, help_text='Entry courses campus')
    # scholars = models.ManyToManyField(Scholar, through='ScholarCourse')
    
    def __str__(self):
        return f'{self.id} : {self.name}'
    

class Subject(models.Model):
    """ Asignatura/Materia """
    # id
    name = models.CharField(max_length=150, help_text='Entry name subject')
    status = models.BooleanField(default=True, help_text='Entry status subject')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, help_text='Entry subjects course')
    # calificatios = models.ManyToManyField(ScholarCourse, through='ScholarCourseSubject')

    def __str__(self):
        return f'{self.id} | {self.name}'