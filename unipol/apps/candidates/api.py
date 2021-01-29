from rest_framework import generics

from .models import * 
from .serializers import * 

class CandidateLC(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    # serializer_class = CandidateDetailsSerializer



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

