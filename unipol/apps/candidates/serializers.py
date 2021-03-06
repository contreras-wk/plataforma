from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import (
    Contact, 
    Candidate,
    Direction,
    CallInfo,
    Studies,
    Documents
)


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Direction
        fields = '__all__'


class CallInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallInfo
        fields = '__all__'


class StudiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studies
        fields = '__all__'


class DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = '__all__'


class CandidateDetailsSerializer(serializers.ModelSerializer):
    documents = DocumentsSerializer()
    contact = ContactSerializer()
    direction = DirectionSerializer()
    callinfo = CallInfoSerializer()
    studies = StudiesSerializer()

    class Meta:
        model = Candidate
        fields = '__all__'

   

