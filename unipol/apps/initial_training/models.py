from django.db import models

from apps.scholar.models import Scholar

class InitialTraining(models.Model):

    hours = models.IntegerField()
    end_date = models.DateField()
    qualification = models.IntegerField()
    status = models.BooleanField()

    scholar = models.OneToOneField(Scholar, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.scholar.candidate.curp}'
        


class AcademicPerformance(models.Model):

    date_test_academic = models.DateField()
    status_test_academic = models.BooleanField()

    initial_training = models.OneToOneField(InitialTraining, on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.initial_training.scholar.candidate.curp}'
    