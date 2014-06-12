from django.conf.urls import patterns, include, url

from testingFrontEnd import views
from glinks.views import glink_counter

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', views.my_view, name='my_view'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/'}),
    url(r'^glink/([0-9]+)/$', glink_counter, name="glink_counter")
)
