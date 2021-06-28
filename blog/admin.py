from django.contrib import admin

# Register your models here.
from .models import Blog  # import project class from models.py
admin.site.register(Blog)
