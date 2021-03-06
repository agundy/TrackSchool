from django.conf.urls import *
from django.conf import settings
from django.views.generic import TemplateView
from views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    # admin documentation
    url(r'^admin/doc/',
        include('django.contrib.admindocs.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('courses.urls')),
    url(r'^$', index)
)


debug = getattr(settings, "DEBUG", False)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT}))
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))
    urlpatterns += patterns(
        '',
        (r'^admin/admin/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT + "admin/"}))
