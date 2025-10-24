from django.contrib import admin
from .models import Organization, Station, Log

# Register your models here.

admin.site.register(Organization)
admin.site.register(Station)
admin.site.register(Log)
