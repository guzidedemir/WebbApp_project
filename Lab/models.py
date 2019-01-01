# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project(models.Model):

    Name = models.CharField(max_length=250)
    Budget = models.IntegerField(default=0)
    Workers = models.ManyToManyField("Worker", blank=True)

    def __str__(self):
        return self.Name + "- $" + str(self.Budget)

class Worker(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Age = models.IntegerField(default=0)
    MyProject = models.ForeignKey("Project", blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.FirstName + " " + self.LastName + "," + str(self.Age) + "years old"
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    def __unicode__(self):
        return self.title + "\n" + self.body