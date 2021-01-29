from django.db.models import fields
from rest_framework import serializers

from .models import (
    Scholar,
    Assistance,
    ScholarCourse,
    ScholarCourseSubject
)

class ScholarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scholar
        fields = '__all__'


class AssistenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assistance
        fields = '__all__'


class ScholarCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScholarCourse
        fields = '__all__'


class ScholarCourseSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScholarCourseSubject
        fields = '__all__'