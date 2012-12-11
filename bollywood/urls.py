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
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
	#adding new view as homepage to display shows
	url(r'^$', 'shows.views.home_page'),
    url(r'^show/$', 'shows.views.show_list'),
    url(r'^show/(?P<show_slug>[-\w]+)/$', 'shows.views.show_detail'),
    url(r'^show/(?P<show_slug>[-\w]+)/(?P<episode_id>[-\w]+)$', 'shows.views.episode_detail'),
    url(r'^movie/$', 'shows.views.movie_list'),
    url(r'^movie/(?P<movie_slug>[-\w]+)/$', 'shows.views.movie_detail'),
    url(r'^accounts/', include('userena.urls')),  
    url(r'^playlist/(?P<show_slug>[-\w]+)/(?P<episode_id>[-\w]+)$', 'shows.views.show_playlist'),
)
