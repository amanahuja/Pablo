# -*- coding:utf-8 -*-
"""
Created on Nov 1, 2010

@author: Aman
"""

from numpy.random import rand
from numpy import floor
from pablo.sentence.models import *

def prepTestData():
    global nouns, verbs, adjectives, prepositions, pronouns, articles

    nouns = ['cow\n', 'dog\n']
    verbs = ['ate\n']
    adjectives = ['small\n']
    prepositions = ['on\n']
    pronouns = ['that\n']
    articles = ['the\n', 'a\n']

    global sentence
    sentence = []

def getArticle():
    nwords = Article.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Article.objects.all()[choose].word
    word_sel = [str(word_sel)]
    
    return word_sel
    
def getAdjective():
    nwords = Adjective.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Adjective.objects.all()[choose].word
    word_sel = [str(word_sel)]
    return word_sel

def getNoun():
    nwords = Noun.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Noun.objects.all()[choose].word
    word_sel = [str(word_sel)]
    return word_sel

def getRelativePronoun():    
    nwords = Pronoun.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Pronoun.objects.all()[choose].word
    word_sel = [str(word_sel)]
    return word_sel

def getPreposition():
    nwords = Preposition.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Preposition.objects.all()[choose].word
    word_sel = [str(word_sel)]
    return word_sel

def getVerb():
    nwords = Verb.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Verb.objects.all()[choose].word
    word_sel = [str(word_sel)]
    return word_sel

def formatString(sentence):
    ss = ''
    for ii in range(len(sentence)):
        ss += sentence[ii]
        ss += ' '
    ss = ss.replace('\n', '')
    ss = ss.capitalize()
    ss = ss.strip()
    ss += '.'
    return ss

