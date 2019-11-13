from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/(?P<id>\d+)$', views.view),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^authors', views.authors),
    url(r'^author/(?P<author_id>\d+)$', views.author_view),
    url(r'^author_delete/(?P<author_id>\d+)$', views.author_delete),

]