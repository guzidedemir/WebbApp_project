# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Lab import forms, models
from forms import BlogsForm
from models import Worker, Project,Blogs
from django.template import RequestContext


def Home(request):
    return render_to_response("home.html")

def DisplayProject(request):
    a = {"projects": models.Project.objects.all()}
    return render(request, "ProjectsAll.html",a)

def DisplaySingleProject(request,PrimaryKey1):
    ProjectName = models.Project.objects.get(Name=PrimaryKey1)

    #projectworkers = models.Project.Workers.all()

    singleproject={"projectname": ProjectName, "projectworkers":ProjectName.Workers.all()}
    return render(request,"SingleProject.html",singleproject)

def DisplayInt(request,integer):
    return HttpResponse(str(integer))

def DisplayWorkers(request):
    b = {"workers":models.Worker.objects.all()}
    s = ""
    id = 1

    for i in models.Worker.objects.all():
        s += "<a href = \"" + str(id) + "\"> " + str(i) + "</a> <br>"
        id += 1
    #return HttpResponse(s)
    return render(request, "AllPeople.html", b)

def DisplaySingleWorker(request, PrimaryKey):
    PrimaryKey1 = PrimaryKey.split("_")
    PrimaryKey1=PrimaryKey1[0]
    WorkerName = models.Worker.objects.get(FirstName=PrimaryKey1)
    person = {"person": WorkerName}
    return render(request, "SingleWorker.html", person)

def DisplayBlogs(request):
    return render(request, "Blogs.html")

def Create_Blog(request):
    c = {"name": request.POST.get("inputname"), "comment":request.POST.get("comments")}
    return render(request, "create_blogs.html", c)

def CreateNew(request):
    if request.method == "POST":
        print request.POST
        form = BlogsForm(request.POST)
    if form.is_valid():
        a = Blogs(title=form.cleaned_data["title"],
                  body=form.cleaned_data["body"])
        a.save()
        return HttpResponseRedirect('/Blogs/')
    else:
        form = BlogsForm()
        context = {'inputform':form}
        return render(request,'new_comment.html',context)




