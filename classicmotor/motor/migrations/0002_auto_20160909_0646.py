# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-09 06:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sighting', to=settings.AUTH_USER_MODEL),
        ),
    ]
