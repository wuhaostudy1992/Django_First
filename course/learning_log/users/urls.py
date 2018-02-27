"""Defines URL patterns for uses"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #Login page
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    
    #Login page
    url(r'^logout/$', views.logout_view, name='logout'),
    
    #Registeration page
    url(r'^register/$', views.register, name='register'),
]
