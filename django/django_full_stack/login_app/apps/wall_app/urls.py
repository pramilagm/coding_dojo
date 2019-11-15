from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'messages$', views.post_message),
    url(r'comments$',views.post_comment),
    url(r'delete$',views.delete_post),
    url(r'logout$',views.logout)
]