
from django.conf.urls import patterns, include, url


from django.conf.urls import patterns, include, url
from library_profile.views import registerlibuser

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netyap.views.sample-app', name='sample-app'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', registerlibuser, name='register'),

)