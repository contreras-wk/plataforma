from django.db.models import query
from django.http import response
from django.http.response import JsonResponse
from rest_framework import generics
from django.http import HttpResponse
           
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from unipol.settings.local import MEDIA_ROOT
 

from .models import * 
from .serializers import * 

class CandidateLC(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    # serializer_class = CandidateDetailsSerializer

class CandidateDetails(generics.RetrieveAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateDetailsSerializer

class DocumentsC(generics.CreateAPIView):
    serializer_class = DocumentsSerializer

class DocumentsRU(generics.RetrieveUpdateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class ContactC(generics.CreateAPIView):
    serializer_class = ContactSerializer

class ContactRU(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class DirectionC(generics.CreateAPIView):
    serializer_class = DirectionSerializer

class DirectionRU(generics.RetrieveUpdateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class StudiesC(generics.CreateAPIView):
    serializer_class = StudiesSerializer

class StudiesRU(generics.RetrieveUpdateAPIView):
    queryset = Studies.objects.all()
    serializer_class = StudiesSerializer


class CallInfoC(generics.CreateAPIView):
    serializer_class = CallInfoSerializer

class CallInfoRU(generics.RetrieveUpdateAPIView):
    queryset = CallInfo.objects.all()
    serializer_class = CallInfoSerializer


class GetDocument(APIView):

  def get(self, request, document):
    path_dake = "/home/luis/Escritorio/plataforma/unipol/media/documents/webcomponents-cheatsheet-2021-lenguajejs.com_FdKjn4d.pdf"
    #         res['file'] = pdf
    #         res['Content-Type'] = 'application/pdf'
    #         res['Content-Disposition'] = f'filename="{file_name}"'
    #         return Response(res, status=200)
    # except Exception as e:
    #     return Response({e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    try:
      file_name = document.split('/')[-1]
      file_path = f'{MEDIA_ROOT}/documents/{file_name}'
      with open(file_path, 'rb') as file:
        pdf = file.read()
        file.close()
        response = HttpResponse(pdf, content_type="application/pdf")
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except Exception as e:
        return Response({e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 