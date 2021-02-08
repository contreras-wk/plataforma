from rest_framework import generics
from rest_framework.fields import get_error_detail

from .models import(
    MedicalAppointment
)

from .serializers import (
    MedicalAppointmentSerializer
)

class MedicalAppointmentCL(generics.ListCreateAPIView):
    queryset = MedicalAppointment.objects.all()
    serializer_class = MedicalAppointmentSerializer


class MerdicalAppointmentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalAppointment.objects.all()
    serializer_class = MedicalAppointmentSerializer

