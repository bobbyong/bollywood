from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import Show, Episode, Movie, Genre, MTV

from django.http import Http404

def home_page(request):
	shows = Show.objects.all()
	movies = Movie.objects.all()
	genres = Genre.objects.all()
	return render_to_response('homepage.html',
            				{'shows': shows, 'movies': movies, 'genres': genres},
                            context_instance=RequestContext(request))



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


def show_playlist(request, show_slug, episode_id):
    try:
        show = Show.objects.get(show_slug_name=show_slug)
        episode = Episode.objects.get(id = episode_id)
    except Show.DoesNotExist:
        raise Http404
    return render_to_response('showplaylist.html',
                            {'show': show, 'episode': episode},
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
        movie = Movie.objects.get(movie_slug_name=movie_slug)
    except Movie.DoesNotExist:
        raise Http404
    return render_to_response('moviedetail.html',
                            {'movie': movie},
                            context_instance=RequestContext(request))


def mtv(request, mtv_id):
    try:
        mtv = MTV.objects.get(id = mtv_id)
    except MTV.DoesNotExist:
        raise Http404
    return render_to_response('mtv.html',
                            {'mtv': mtv},
                            context_instance=RequestContext(request))
