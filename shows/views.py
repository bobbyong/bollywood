from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import Show


def show_list(request):
	shows = Show.objects.all()
	
	return render_to_response('showlist.html',
            				{'shows': shows},
                            context_instance=RequestContext(request))

def show_page(request):
	pass
