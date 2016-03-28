
from django.conf.urls import patterns, include, url
from library_profile.views import myprofile,reqdeleteconfirm,reqdeletdone

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netyap.views.sample-app', name='sample-app'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', myprofile, name='myprofile'),
    url(r'^delreqconfirm/$', reqdeleteconfirm, name='delreqconfirm'),
    url(r'^delreqdone/$', reqdeletdone, name='delreqdone'),
)