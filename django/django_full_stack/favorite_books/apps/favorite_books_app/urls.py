from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^login$', views.login),
    url(r'^books$',views.books),
    url(r'^books/add$',views.books_add),
    url(r'^books/add_favorite/(?P<book_id>\d+)$',views.add_favorite),
    url(r'^books/show/(?P<book_id>\d+)$',views.show_book_info),
    url(r'^books/show/(?P<book_id>\d+)/edit$',views.book_edit),
    url(r'^books/show/(?P<book_id>\d+)/delete$',views.book_delete),
    url(r'^books/show/(?P<book_id>\d+)/unfavorite$',views.unfavorite),
    url(r'^books/show/(?P<book_id>\d+)/favorite$',views.add_favorite_book),
    url(r'books/display',views.display),
    url(r'^books/logout$',views.logout)
]