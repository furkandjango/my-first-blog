from django.conf.urls import url
from .views import *

app_name='post'


urlpatterns = [
    url(r'^index/$',post_index,name="index"),
    url(r'^create/$', post_create,name="create"),
    url(r'^(?P<slug>[\w-]+)/$', post_detail,name="detail"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete,name="delete"),
    url(r'^(?P<slug>[\w-]+)/update/$',post_update,name="update"),


]