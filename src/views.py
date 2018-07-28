# Create your views here.

from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request)    
    return HttpResponse(t.render(c))

def construct(request):
    t = loader.get_template('construct.html')
    c = RequestContext(request)    
    return HttpResponse(t.render(c))    