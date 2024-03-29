"""cache_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from cache_server_app import api

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cache_server/', include('cache_server_app.urls')),
    url(r'^cache_server/$',
        api.CacheDetails.as_view(),
        name="cache"),
    url(r'^cache_server/(?P<md5>\S{32})$',
        api.CacheDetails.as_view(),
        name="cacheDetail"),
    url(r'^cache_server/upload/$', api.UploadFile.as_view(), name="uploadFile"),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
