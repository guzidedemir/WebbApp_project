# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.contrib import admin


admin.site.register(models.Project)
admin.site.register(models.Worker)
