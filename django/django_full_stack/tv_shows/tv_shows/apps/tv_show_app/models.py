from __future__ import unicode_literals
from django.db import models

from datetime import datetime,date
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
       
        if len(postData['title']) < 3:
            errors["name"] = " Show Title name should be at least 2 characters"
        if len(postData['network'])<4:
            errors['network'] = " Show Network name should be at least 3 characters"
        if len(postData['desc']) < 11:
            errors["desc"] = "Show description should be at least 10 characters"
        if len(postData["release_date"]) > 0 and datetime.strptime(postData["release_date"], '%Y-%m-%d') > datetime.today() :
            errors["release_date"] = "Invalid release date."
        return errors


class Tv_show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length =255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

