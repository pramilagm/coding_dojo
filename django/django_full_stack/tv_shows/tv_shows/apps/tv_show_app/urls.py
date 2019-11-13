from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.new),
    url(r'^shows/new/create$', views.create),
    url(r'^shows/(?P<show_id>\d+)$',views.view),
    url(r'^shows/(?P<show_id>\d+)/edit$',views.show_edit),
    url(r'^shows/(?P<show_id>\d+)/update$', views.show_edit_update),
    url(r'^shows/(?P<show_id>\d+)/destroy$',views.show_destroy)
]