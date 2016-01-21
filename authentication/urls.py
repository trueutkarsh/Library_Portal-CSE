__author__ = 'trueutkarsh'

from django.conf.urls import patterns, include, url
from authentication import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netyap.views.sample-app', name='sample-app'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^login/', views.authentication, name='login'),
    url(r'^logout/', views.logout, name='logout'),
)
