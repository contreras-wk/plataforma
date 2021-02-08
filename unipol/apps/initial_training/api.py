from rest_framework import generics

from .models import (
   InitialTraining,
   AcademicPerformance
)

from .serializers import (
    InitialTrainingSerializer,
    AcademicPerformanceSerializer
)

class InitialTrainingLC(generics.ListCreateAPIView):
    queryset = InitialTraining.objects.all()
    serializer_class = InitialTrainingSerializer


class InitialTrainingRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = InitialTraining.objects.all()
    serializer_class = InitialTrainingSerializer


class AcademicPerformanceLC(generics.ListCreateAPIView):
    queryset = AcademicPerformance.objects.all()
    serializer_class = AcademicPerformanceSerializer


class AcademicPerformanceRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AcademicPerformance.objects.all()
    serializer_class = AcademicPerformanceSerializer