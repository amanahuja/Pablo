from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from pablo.sentence.models import Word

def index(request):
    return HttpResponse("Hello, world. You're at the sentence index.")


def getFancyNoun():
    pass
