from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [

    path('index/', post_index,name='index'),
    url(r'^(?P<id>\d+)/$', post_detail,name='details'),
    path('create/', post_create,name='create'),
    url(r'^(?P<id>\d+)/update/$', post_update,name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete,name='delete'),




]