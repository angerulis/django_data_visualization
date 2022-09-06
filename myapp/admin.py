from django.contrib import admin

from .models import Education, Transport

admin.site.register([Education, Transport])
