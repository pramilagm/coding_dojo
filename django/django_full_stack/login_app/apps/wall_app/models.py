from django.db import models

from apps.users_login_app.models import Form

class Messages(models.Model):
    message = models.TextField()
    user = models.ForeignKey(Form,related_name = 'messages')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comments(models.Model):
    comments = models.TextField()
    message = models.ForeignKey(Messages,related_name="user_comments")
    user = models.ForeignKey(Form, related_name='user_comments')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

