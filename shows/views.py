from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import Show

from django.http import Http404

def list(request):
	shows = Show.objects.all()
	
	return render_to_response('showlist.html',
            				{'shows': shows},
                            context_instance=RequestContext(request))

def detail(request, slug):
    try:
        show = Show.objects.get(show_slug_name=slug)
    except Show.DoesNotExist:
        raise Http404
    return render_to_response('showdetail.html',
            				{'show': show},
                            context_instance=RequestContext(request))