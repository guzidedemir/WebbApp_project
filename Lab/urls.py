from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

from django.contrib import admin
from django.utils.text import slugify

from . import views

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^/(?P<integer>[0-9]+)',views.DisplayInt),
    url(r'^/Project/$', views.DisplayProject),
    url(r'^/Project/(?P<PrimaryKey1>[a-z|A-z]+)', views.DisplaySingleProject),
    url(r'^/People/$', views.DisplayWorkers),
    url(r'^/People/(?P<PrimaryKey>[a-z|A-z]+)', views.DisplaySingleWorker),
    url(r'^/Blogs/$', views.DisplayBlogs),
    url(r'/Create/$', views.Create_Blog)

]