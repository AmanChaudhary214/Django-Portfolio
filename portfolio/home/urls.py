from django.contrib import admin
from django.urls import path, include
from home import views


#Django admin header customizations

admin.site.site_header = "Login to Aman's Portal"
admin.site.site_title = "Welcome to Aman's Dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('skills', views.skills, name='skills'),
    path('projects', views.projects, name='projects'),
    path('statistics', views.statistics, name='statistics'),
    path('contact', views.contact, name='contact')
]