#from django.contrib import admin
from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from . import views  # used . becoz views and url are in same folder(blog)

urlpatterns = [

               path('', views.all_blogs, name='all_blogs'),
               path('<int:blog_id>/', views.detail, name='detail')

              ]

app_name='blog'