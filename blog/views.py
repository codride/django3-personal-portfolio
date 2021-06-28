from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def all_blogs(request):
     #pull from database
  
    blogs=Blog.objects.order_by('-date') #most recent blogs and first three
    return render (request,'blog/all_blogs.html',{'blogs':blogs}) # then send  to template

def detail(request,blog_id):
     blog=get_object_or_404(Blog,pk=blog_id)
     return render (request,'blog/detail.html',{'blog':blog})
     
    


    


    
    

