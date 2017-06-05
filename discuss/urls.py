from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<topic_id>[0-9]+)/$', views.details, name='details'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^(?P<topic_id>[0-9]+)/new_comment/$', views.new_comment, name='new_comment'),
]