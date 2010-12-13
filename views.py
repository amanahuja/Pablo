# -*- coding:utf-8 -*-
"""
Created on Nov 3, 2010
    modified Nov 5th to run on both Django and local installs

Views.py 
Renders primary django views for Pablo
    index
Can also be run in test mode on a local machine.
    Unresolved django imports are substituted by local equivalents.  

@author: Aman
"""

try: 
    from django.shortcuts import render_to_response
    from django.template import RequestContext
    from django.http import HttpResponseRedirect
    from django.core.urlresolvers import reverse
    
    from pablo.sentence.create import *
    from pablo.meta.models import *

except ImportError:
    
    from create import getSentence 
    import getFileWords
    
    # the following import is not redundant
    from getFileWords import formatString, prepTestData, prepData

'''
-----------------------------------------------------------------
Django views here. 
'''
    
def index(request):

    #prepData()
    sentence = getSentence()
    sentence = sentence.content
    sentence = formatString(sentence)

    #sentence = "Adjective noun verb preposition article noun."
    return render_to_response('index.html', {'sentence': sentence}, 
                               context_instance=RequestContext(request))

def store(request):
    '''
    Stores (saves) the sentence sent by POST data from the index view
    Redirect View only
    '''
    saved = Bestseller()
    saved.sentence = request.POST['saved']
    saved.save()
    return HttpResponseRedirect(reverse('pablo.views.saved', args=(saved.id,)))

def vote(request, sid):
    '''
    Increments vote count of a sentence
    Redirect View only
    '''
    s = Bestseller.objects.get(id=sid)
    
    votechk = 'has_voted_' + str(sid)
    if not votechk in request.session:
        s.votes = s.votes + 1
        s.save()
        request.session[votechk] = True

    return HttpResponseRedirect(reverse('pablo.views.saved', args=(s.id,)))

def saved(request, sid):
    '''
    Display a Saved Sentence
    '''

    saved = Bestseller.objects.get(id=sid)

    return render_to_response('saved.html', {'sentence': saved.sentence,
                        'save_date': saved.save_date,
                        'votes': saved.votes,
                        'sid': saved.id})

def savedlist(request):
    '''
    Display a list of saved sentences
    '''
    bslist = Bestseller.objects.extra(order_by = ['-votes'])

    return render_to_response('bestsellers.html', {'bslist': bslist})

'''
-----------------------------------------------------------------
Local non-Django environment execution
'''

def main():
    #getFileWords.prepData()
    getFileWords.prepTestData()
    
    sentence = getSentence()
    sentence = sentence.content
    sentence = getFileWords.formatString(sentence)
    print sentence

if __name__ == "__main__":
    for ii in range(10):
        main()
    
