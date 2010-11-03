from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from pablo.sentence.models import *
from pablo.sentence.create import *
from numpy.random import rand
from numpy import floor

def index(request):

    sentence = []

    sentence = getFancyNoun()
    sentence = formatString(sentence)

    #sentence = "Adjective noun verb preposition article noun."
    return render_to_response('index.html', {'sentence': sentence})
