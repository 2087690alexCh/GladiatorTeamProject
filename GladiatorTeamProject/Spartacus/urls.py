from django.conf.urls import patterns, url
from Spartacus import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_profile/$', views.add_profile, name='add_profile'),)
