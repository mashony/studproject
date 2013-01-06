from django.contrib import admin
from app.models import *
from app.auth.models import ActivateProfile

admin.site.register(Student)
admin.site.register(Group)

admin.site.register(ActivateProfile)
