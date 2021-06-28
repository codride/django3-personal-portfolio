from django.contrib import admin

# Register your models here.

from .models import Project  # import project class from models.py
admin.site.register(Project)  # hey , I want to see this model inside the admin


"""
first step of creating a app is Going to the admin and
 register with the admin page and then getting them to 
show up inside the templates




"""
