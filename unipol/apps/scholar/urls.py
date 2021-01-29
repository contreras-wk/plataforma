from django.urls import path

from .api import (
    ScholarLC,
    ScholarRUD,
    AssistenceLC,
    AssistenceRUD,
    ScholarCourseLC,
    ScholarCourseRUD,
    ScholarCourseSubjectLC,
    ScholarCourseSubjectRUD
)


urlpatterns = [
    path('scholars/', ScholarLC.as_view(), name='scholars'),
    path('scholar/<int:pk>/', ScholarRUD.as_view(), name='scholar_details'),

    path('assistences/', AssistenceLC.as_view(), name='assistences'),
    path('assistence/<int:pk>/', AssistenceRUD.as_view(), name='assistence_details'),

    path('scholar_courses/', ScholarCourseLC.as_view(), name='scholar_courses'),
    path('scholar_course/<int:pk>/', ScholarCourseRUD.as_view(), name='sholar_course_details'),

    path('scholar_course_subjects/', ScholarCourseSubjectLC.as_view(), name='scholar_course_subjects'),
    path('scholar_course_subjects/<int:pk>/', ScholarCourseSubjectRUD.as_view(), name='scholar_course_subjects_details',)

]
