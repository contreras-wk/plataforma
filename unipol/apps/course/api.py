from rest_framework import generics
from rest_framework.views import APIView

from .models import (
    Subject,
    Zone,
    Course,
    Campus
)

from .serializers import (
    SubjectSerializer,
    ZoneSerializer,
    CourseSerializer,
    CampusSerializer
)


class SubjetLC(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjetRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ZoneLC(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class ZoneRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class CourseLC(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CampusLC(generics.ListCreateAPIView):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class CampusRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer







# class TeachersLC(generics.ListCreateAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer


# class TeacherRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer


# class CoursesLC(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# class CourseRU(generics.RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# class GroupLC(generics.ListCreateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# class GroupRU(generics.RetrieveUpdateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# class ScheduleLC(generics.ListCreateAPIView):
#     queryset = Schedule.objects.all()
#     serializer_class = ScheduleSerializer


# class ScheduleRU(generics.RetrieveUpdateAPIView):
#     queryset = Schedule.objects.all()
#     serializer_class = ScheduleSerializer

# """ ADDD """
# class CourseGroupLC(generics.ListCreateAPIView):
#     queryset = CourseGroup.objects.all()
#     serializer_class = CourseGroupSerializer


# class CourseGroupRU(generics.RetrieveUpdateAPIView):
#     queryset = CourseGroup.objects.all()
#     serializer_class = CourseGroupSerializer


# class GroupShedulerLC(generics.ListCreateAPIView):
#     query = GroupScheduler.objects.all()
#     serializer_class = GroupSchedulerSerializer


# class GroupShedulerRU(generics.RetrieveUpdateAPIView):
#     query = GroupScheduler.objects.all()
#     serializer_class = GroupSchedulerSerializer

# class AssistenceLC(generics.ListCreateAPIView):
#     queryset = Assistence.objects.all()
#     serializer_class = AssistenceSerializer

# class AssistenceRU(generics.RetrieveUpdateAPIView):
#     queryset = Assistence.objects.all()
#     serializer_class = AssistenceSerializer
