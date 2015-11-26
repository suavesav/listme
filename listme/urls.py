from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from listme.views import api

admin.autodiscover()

urlpatterns = patterns('',
                       url(
                           r'^api/$', api.api_root
                       ),
                       url(
                           r'^api/lists/$', api.ListList.as_view(),
                           name='list-list'
                       ),
                       url(
                           r'^api/lists/(?P<pk>\d+)/$', api.ListDetail.as_view()
                       ),
                       url(
                           r'^api/users/$', api.UserList.as_view(),
                           name='user-list'
                       ),
                       url(
                           r'^api/users/(?P<pk>\d+)/$', api.UserDetail.as_view()
                       ),
                       url(
                           r'^admin/', include(admin.site.urls)
                       ),
)

#TODO define the operations for each page on a controller for that page
urlpatterns += patterns(
                        url(
                           r'^lists/$', api.api_root
                       ),
                        url(
                           r'^lists/(?P<pk>\d+)/$', api.ListDetail.as_view()
                       ),
                        url(
                           r'^u/(?P<user_pk>\d+)/lists$', api.ListDetail.as_view()
                       ),
                        url(
                           r'^u/(?P<user_pk>\d+)/lists/(?P<list_pk>\d+)$', api.ListDetail.as_view()
                       ),
)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-login/', include('rest_framework.urls',
                               namespace='rest_framework')),
]