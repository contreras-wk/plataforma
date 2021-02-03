from django.db import models

from apps.scholar.models import Scholar

class MedicalAppointment(models.Model):

    date_medical_appointment = models.DateField()
    consulting_room = models.CharField(max_length=6)
    date_results = models.DateField()
    results = models.TextField()
    status_appointment = models.BooleanField()
    status_patient = models.BooleanField()
    
    scholar = models.OneToOneField(Scholar, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.scholar.candidate.curp}'
    
