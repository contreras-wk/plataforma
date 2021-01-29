from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import (
    Subject,
    Zone,
    Course,
    Campus
)


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zone
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

        class Meta:
            model = Course
            fields = '__all__'


class CampusSerializer(serializers.ModelSerializer):

    # courses = CourseSerializer()

    class Meta:
        model = Campus
        fields = '__all__'
