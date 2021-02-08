from django.urls import path

from .api import (
    MedicalAppointmentCL,
    MerdicalAppointmentRUD
)

urlpatterns = [
    path('medical_appointment/', MedicalAppointmentCL.as_view(), name='medical_appointment'),
    path('medical_appointment/<int:pk>/', MerdicalAppointmentRUD.as_view(), name='medical_appointment_details'),
]