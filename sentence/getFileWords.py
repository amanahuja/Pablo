# -*- coding:utf-8 -*-
"""
Created on Nov 1, 2010

This package fetches words for non-django using environments. 
PrepTestData loads a miniword list for testing. 
PrepData loads wordlists from text files in folder /pos

@author: Aman
"""

#Import numpy or pylab, as available. 
try: 
    from numpy.random import rand
    from numpy import floor
except ImportError:
    from pylab import rand, floor
   
def prepData():
    global nouns, verbs, adjectives, prepositions, pronouns, articles

    try:     
        nounfile = open('pos/nouns.txt', 'r')
        nouns = nounfile.readlines()
        nounfile.close()
    
        verbfile = open('pos/verbs.txt', 'r')
        verbs = verbfile.readlines()
        verbfile.close()
    
        adjfile = open('pos/adjectives.txt', 'r')
        adjectives = adjfile.readlines()
        adjfile.close()
    
        prepofile = open('pos/prepositions.txt', 'r')
        prepositions = prepofile.readlines()
        prepofile.close()
    
        pnounfile = open('pos/pronouns.txt', 'r')
        pronouns = pnounfile.readlines()
        pnounfile.close()
    
        artfile = open('pos/articles.txt', 'r')
        articles = artfile.readlines()
        artfile.close()
    except IOError:
        print "POS files not found. Using Test Data."
        prepTestData()
        
def prepTestData():
    global nouns, verbs, adjectives, prepositions, pronouns, articles

    nouns = ['cow\n', 'apple']
    verbs = ['ate\n']
    adjectives = ['big\n']
    prepositions = ['on\n']
    pronouns = ['that\n']
    articles = ['the\n', 'a']
    
def getArticle(): 
    choose = int(floor(rand() * len(articles)))
    return articles[choose]

def getAdjective():
    choose = int(floor(rand() * len(adjectives)))
    return adjectives[choose]
    
def getNoun():
    choose = int(floor(rand() * len(nouns)))
    return nouns[choose]
    
def getRelativePronoun():
    choose = int(floor(rand() * len(pronouns)))
    return pronouns[choose]
    
def getPreposition():
    choose = int(floor(rand() * len(prepositions)))
    return prepositions[choose]
    
def getVerb():
    choose = int(floor(rand() * len(verbs)))
    return verbs[choose]

def formatString(sentence):
    ss = ''
    for ii in range(len(sentence)):
        ss += sentence[ii]
        ss += ' '
    ss = ss.replace('\n', ' ')
    ss = ss.capitalize()
    ss = ss.strip()
    ss += '.'
    return ss

