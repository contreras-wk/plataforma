from django.urls import path

from .api import(
    InitialTrainingLC,
    InitialTrainingRUD,
    AcademicPerformanceLC,
    AcademicPerformanceRUD
)

urlpatterns = [
    path('initial_training/', InitialTrainingLC.as_view(), name='initial_training'),
    path('initial_training/<int:pk>/', InitialTrainingRUD.as_view(), name='initial_training_details'),

    path('academic_performance/', AcademicPerformanceLC.as_view(), name='academic_perfonrmance'),
    path('academic_performance/<int:pk>/', AcademicPerformanceRUD.as_view(), name='academic_perfonrmance_details'),
]
