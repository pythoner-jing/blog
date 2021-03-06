from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from app.views import * 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", index),
    url(r"^tech/$", tech),
    url(r"^proj/$", proj),
    url(r"^misc/$", misc),
    url(r"^login/$", login),
    url(r"^logout/$", logout),
    url(r"^distribute/$", distribute),
    url(r"^read/([^/]+)/$", read),
    url(r"^delete/([^/]+)/$", delete),
    url(r"^edit/([^/]+)/$", edit),
    url(r"^tag/([^/]+)/$", tag),
)
