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


def episode_detail(request, show_slug, episode_id):
    try:
        episode = Episode.objects.get(id = episode_id)
    except Show.DoesNotExist:
        raise Http404
    return render_to_response('episodedetail.html',
            				{'episode': episode},
                            context_instance=RequestContext(request))


def movie_list(request):
    movies = Movie.objects.all()
    
    return render_to_response('movielist.html',
                            {'movies': movies},
                            context_instance=RequestContext(request))

def movie_detail(request, movie_slug):
    try:
        movie = Movie.objects.get(show_movie_name=movie_slug)
    except Movie.DoesNotExist:
        raise Http404
    return render_to_response('moviedetail.html',
                            {'movie': movie},
                            context_instance=RequestContext(request))