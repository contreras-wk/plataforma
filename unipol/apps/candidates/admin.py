from django.contrib import admin

from .models import (
    Candidate,
    Documents,
    Contact,
    Direction,
    CallInfo,    
    Studies,
)

admin.site.register(Candidate)
admin.site.register(Documents)
admin.site.register(Contact)
admin.site.register(Direction)
admin.site.register(CallInfo)
admin.site.register(Studies) 