from django.contrib import admin


from .models import (
    Assistance,
    Scholar,
    ScholarCourse,
    ScholarCourseSubject
)
admin.site.register(Assistance)
admin.site.register(Scholar)
admin.site.register(ScholarCourse)
admin.site.register(ScholarCourseSubject)
