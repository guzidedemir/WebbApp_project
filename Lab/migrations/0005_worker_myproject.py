# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0004_remove_worker_myproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='MyProject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Lab.Project'),
        ),
    ]