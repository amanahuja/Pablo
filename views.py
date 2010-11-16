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
    from pablo.sentence.create import *

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
    return render_to_response('index.html', {'sentence': sentence})


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
    
