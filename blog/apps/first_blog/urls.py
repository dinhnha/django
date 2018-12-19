from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new), 
    url('^create$', views.create), 
    url('^(?P<number>\d+)$', views.show),
    url('^(?P<number>\d+)/edit$', views.edit), 
    url('^(?P<number>\d+)/delete$', views.destroy)
] 