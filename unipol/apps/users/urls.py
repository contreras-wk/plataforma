from django.urls import path

from .api import (
    RoleLC,
    RoleRUD,
    PermissionLC,
    PermissionRUD,
    UserLC,
    UserRUD,
    InstitutionLC,
    InstitutionRUD,
    UserPermisionLC,
    UserPermisionRUD
)

urlpatterns = [
    path('roles/', RoleLC.as_view(), name='roles'),
    path('role/<int:pk>/', RoleRUD.as_view(), name='role_details'),

    path('permissions/', PermissionLC.as_view(), name='permisions'),
    path('permission/<int:pk>/', PermissionRUD.as_view(), name='permision_details'),

    path('users/', UserLC.as_view(), name='users'),
    path('user/<int:pk>/', UserRUD.as_view(), name='users_details'),

    path('institutions/', InstitutionLC.as_view(), name='institutions'),
    path('institution/<int:pk>/', InstitutionRUD.as_view(), name='institution_details'),

    path('user_permisions/', UserPermisionLC.as_view(), name='user_permisions'),
    path('user_permision/<int:pk>/', UserPermisionRUD.as_view(), name='user_permisions_details'),
]
