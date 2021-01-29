from django.db import models
from rest_framework import fields, serializers

from .models import (
    Role,
    Permission,
    User,
    Institution,
    UserPermision
)

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = '__all__'


class UserPermissionSeriaizer(serializers.ModelSerializer):

    class Meta:
        model = UserPermision
        fields = '__all__'