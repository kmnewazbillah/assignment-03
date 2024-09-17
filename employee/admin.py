# employee/admin.py
from django.contrib import admin
from .models import Employee


# Register the Employee model with custom admin
admin.site.register(Employee)
