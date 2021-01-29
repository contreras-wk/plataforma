from django.contrib import admin

from .models import (
    Role,
    Permission,
    Institution,
    User,
    UserPermision
)

admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Institution)
admin.site.register(User)
admin.site.register(UserPermision)