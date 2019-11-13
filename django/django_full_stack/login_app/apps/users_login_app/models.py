

from __future__ import unicode_literals
from django.db import models
import re


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name'])<3:
            errors["last_name"] = "Last name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        if postData['password']!=postData['cnpassword']:
            errors['password'] ="Password Doesnot Match"
        if len(postData['password'])<9:
            errors['password'] = "Password must be at least 8 characters"
        return errors


class Form(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()  