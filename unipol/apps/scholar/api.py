

from rest_framework import generics

from .models import (
    Scholar,
    Assistance,
    ScholarCourse,
    ScholarCourseSubject
)

from .serializers import (
    ScholarSerializer,
    AssistenceSerializer,
    ScholarCourseSerializer,
    ScholarCourseSubjectSerializer
)

class ScholarLC(generics.ListCreateAPIView):
    queryset = Scholar.objects.all()
    serializer_class = ScholarSerializer


class ScholarRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scholar.objects.all()
    serializer_class = ScholarSerializer


class AssistenceLC(generics.ListCreateAPIView):
    queryset = Assistance.objects.all()
    serializer_class = AssistenceSerializer


class AssistenceRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assistance.objects.all()
    serializer_class = AssistenceSerializer


class ScholarCourseLC(generics.ListCreateAPIView):
    queryset = ScholarCourse.objects.all()
    serializer_class = ScholarCourseSerializer


class ScholarCourseRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScholarCourse.objects.all()
    serializer_class = ScholarCourseSerializer


class ScholarCourseSubjectLC(generics.ListCreateAPIView):
    queryset = ScholarCourseSubject.objects.all()
    serializer_class = ScholarCourseSubjectSerializer

class ScholarCourseSubjectRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScholarCourseSubject.objects.all()
    serializer_class = ScholarCourseSubjectSerializer




