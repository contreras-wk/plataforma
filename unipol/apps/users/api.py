from rest_framework import generics, serializers

from .models import (
    Role,
    Permission,
    User,
    Institution,
    UserPermision
)

from .serializers import (
    RoleSerializer,
    PermissionSerializer,
    UserSerializer,
    InstitutionSerializer,
    UserPermissionSeriaizer
)


class RoleLC(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PermissionLC(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class PermissionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserLC(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InstitutionLC(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class UserPermisionLC(generics.ListCreateAPIView):
    queryset = UserPermision.objects.all()
    serializer_class = UserPermissionSeriaizer


class UserPermisionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPermision.objects.all()
    serializer_class = UserPermissionSeriaizer