# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-08 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='this is the description'),
        ),
    ]