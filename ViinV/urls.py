# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ViinV.views.home', name='home'),
    # url(r'^ViinV/', include('ViinV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Página principal
    url(r'^$', 'cvn.views.main', name='main'),
    
    url(r'^cvn/$', 'cvn.views.index', name='index'),
    # Login/Logout CAS
    url(r'^accounts/login/$', 'django_cas.views.login', name='login'), #{'next_page': ''}),
    url(r'^accounts/logout/$', 'django_cas.views.logout', name='logout'),# {'next_page': '/'}),    

)
