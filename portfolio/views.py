from django.shortcuts import render 
from .models import Project  

# Create your views here.
# Url request 
def home(request):
    projects=Project.objects.all() #extract objects on home page
    return render(request,'portfolio/home.html',{'projects':projects})  
 #first create a folder named template inside portfolio and then create 
 #a folder namd portfolio inside templates and inside this create a file
 #named home.html

