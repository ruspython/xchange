from django.conf.urls import patterns, include, url

from .views import *


urlpatterns = patterns('',
                       url(r'^$', BannerListView.as_view(), name='banners-list'),
                       url(r'^referring/(?P<site_owner_id>[\d]+)/(?P<banner_id>[\d]+)/$', banner_click, name='banner-list'),
)
