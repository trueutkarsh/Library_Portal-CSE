from django.conf.urls import include, url
from django.contrib import admin
from admin_interface.views import *
from django.contrib.sites.models import Site
urlpatterns = [

    url(r'^rtoi/', reqtoissue,name='addtoissuelog'),
    url(r'^rtoi/confirm/', reqtoissueconfirm,name='addtoissuelogconfirm'),
    url(r'^rtoi/done/', reqtoissuedone,name='addtoissuelogconfirm'),

    url(r'^itor/', issuetoreturn,name='issuetoreturn'),
    url(r'^itor/confirm/', issuetoreturnconfirm,name='issuetoreturnconfirm'),
    url(r'^itor/done/', issuetoreturndone,name='issuetoreturnconfirm')


]