from django.urls import path

from .api import (
    SubjetLC,
    SubjetRUD,
    ZoneLC,
    ZoneRUD,
    CourseLC,
    CourseRUD,
    CampusLC,
    CampusRUD
)

urlpatterns = [

    path('subjects/', SubjetLC.as_view(), name='subjets'),
    path('subject/<int:pk>/', SubjetRUD.as_view(), name='subjet_details'),

    path('zones/', ZoneLC.as_view(), name='zones'),
    path('zone/<int:pk>/', ZoneRUD.as_view(), name='zone_details'),

    path('courses/', CourseLC.as_view(), name='courses'),
    path('course/<int:pk>/', CourseRUD.as_view(), name='course_details'),

    path('campus/', CampusLC.as_view(), name='campus'),
    path('campus/<int:pk>/', CampusRUD.as_view(), name='campus_details')

]
