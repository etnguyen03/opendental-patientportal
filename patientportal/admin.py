from django.contrib import admin
from patientportal.apps.users.models import Patient, UserProperties

admin.site.register(Patient)
admin.site.register(UserProperties)