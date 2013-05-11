from django.conf.urls import patterns, url

from map import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

urlpatterns += patterns('',
 (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
 )
