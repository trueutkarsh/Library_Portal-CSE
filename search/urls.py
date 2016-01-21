
#search urls are here
from django.conf.urls import  url
from views import *

urlpatterns = [

    url(r'^$', searchit, name='index'),
    url(r'^issue/', issuebook, name="issue"),

]
