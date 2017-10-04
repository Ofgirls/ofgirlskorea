from django.contrib import admin
from .models import Report

# Register your models here.
# django admin page관련 공부: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
admin.site.register(Report)