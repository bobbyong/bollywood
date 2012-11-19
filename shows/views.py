from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import Show, Episode

from django.http import Http404

def show_list(request):
	shows = Show.objects.all()
	
	return render_to_response('showlist.html',
            				{'shows': shows},
                            context_instance=RequestContext(request))

def show_detail(request, show_slug):
    try:
        show = Show.objects.get(show_slug_name=show_slug)
    except Show.DoesNotExist:
        raise Http404
    return render_to_response('showdetail.html',
            				{'show': show},
                            context_instance=RequestContext(request))


def episode_detail(request, show_slug, episode_slug):
    try:
        show = Show.objects.get(show_slug_name=show_slug)
        episode = Episode.objects.get(episode_slug_name = episode_slug)
    except Show.DoesNotExist:
        raise Http404
    return render_to_response('episodedetail.html',
            				{'episode': episode},
                            context_instance=RequestContext(request))