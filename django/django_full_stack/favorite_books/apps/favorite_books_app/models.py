from __future__ import unicode_literals
from django.db import models

import re


class UserManager(models.Manager):

    def basic_validator(self, postData):    
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):                
            errors['email'] = ("Invalid email address!")
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name'])<3:
            errors["last_name"] = "Last name should be at least 2 characters"
        if postData['password']!=postData['cnpassword']:
            errors['password'] ="Password Doesnot Match"
        if len(postData['password'])<9:
            errors['password'] = "Password must be at least 8 characters"
        return errors

class BookManager(models.Manager):

    def book_validator(self,postData):
        errors = {}
        if len(postData['title']) ==0:
            errors['title'] ="title cannot be empty"
        if len(postData['desc']) < 6:
            errors['title'] ="Description must be atleast 6 character"
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
  # liked_books = a list of books a given user likes
  # books_uploaded = a list of books uploaded by a given user
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User,related_name ="books_uploaded")
    users_who_like = models.ManyToManyField(User,related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
  # uploaded_by = user who uploaded a given book
  # users_who_like = a list of users who like a given book