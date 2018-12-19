from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^process_money/$', views.process_money, name = "process_money"),
    #url(r'^process/$', views.process, name="process"),
    #url(r'^clear/$', views.clear, name="clear")
]