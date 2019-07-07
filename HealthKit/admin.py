from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Language)
admin.site.register(models.UserDetails)
admin.site.register(models.OtherDetails)
admin.site.register(models.PatientRequest)
admin.site.register(models.DoctorResponse)
