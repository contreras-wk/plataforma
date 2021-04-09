from django.urls import path

from django.conf.urls.static import static
from unipol.settings import local

from .api import *
from .views import view_pdf

urlpatterns = [
    path('', CandidateLC.as_view(), name='candidates'),
    path('<int:pk>/', CandidateDetails.as_view(), name='candidate'),
    path('update/<int:pk>/', CandidateRUD.as_view(), name='candidate'),

    path('document/', DocumentsC.as_view(), name='document'),
    path('document/<str:document>/', GetDocument.as_view(), name='document'),
    # path('document/<str:document>/', view_pdf),

    path('contact/', ContactC.as_view(), name='contact'),
    path('contact/<int:pk>/', ContactRU.as_view(), name='contact'),
    
    path('direction/', DirectionC.as_view(), name='direction'),
    path('direction/<int:pk>/', DirectionRU.as_view(), name='direction'),

    path('studie/', StudiesC.as_view(), name='studie'),
    path('studie/<int:pk>/', StudiesRU.as_view(), name='studie'),

    path('call_info/', CallInfoC.as_view(), name='call_info'),
    path('call_info/<int:pk>/', CallInfoRU.as_view(), name='call_info'),
] + static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)
