from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitbits.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bitbits.views.home', name='home'),
    url(r'^bit-item$', 'bitbits.views.update', name='update'),
    url(r'^unit-change$', 'bitbits.views.units', name='units'),
 )
