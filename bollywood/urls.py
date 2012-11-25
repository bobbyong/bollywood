from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bollywood.views.home', name='home'),
    # url(r'^bollywood/', include('bollywood.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', TemplateView.as_view(template_name='home.html')),
    url(r'^$', 'shows.views.show_list'),
    url(r'^show/(?P<show_slug>[-\w]+)/$', 'shows.views.show_detail'),
    url(r'^show/(?P<show_slug>[-\w]+)/(?P<episode_id>[-\w]+)$', 'shows.views.episode_detail'),
)
