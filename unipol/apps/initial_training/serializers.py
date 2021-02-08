from django.db.models import fields
from rest_framework import serializers

from .models import (
   InitialTraining,
   AcademicPerformance
)

class InitialTrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = InitialTraining
        fields = '__all__'


class AcademicPerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcademicPerformance
        fields = '__all__'