
from pablo.sentence.models import *

from numpy.random import rand
from numpy import floor

'''
Created on Oct 04, 2010
Pablo the random sentence generator

TODO:
 Create a method to collect and store feedback on sentences and words.

@author: Aman
'''

nouns = None
verbs = None
adjectives = None
prepositions = None
pronouns = None
articles = None
sentence = []

def getFancyNoun():
    global sentence
    #sentence = ["Taking a nap. Please come back later."] 

    getOrnateNoun()

    pos = floor(rand() * 4)
    if pos == 0:
        getRelativePronoun()
        getVerb()
        getOrnateNoun()
    if pos == 1:
        getRelativePronoun()
        getOrnateNoun()
        getVerb()
    if pos == 2:
        pass
    if pos == 3:
        getPreposition()
        getFancyNoun()

    return sentence

def getOrnateNoun():
    pos = floor(rand() * 3)
    if pos == 0:
        getArticle()
    if pos == 1:
        getAdjective()
    if pos == 2:
        getNoun()

def getArticle():
    global sentence
    global articles

    nwords = Article.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Article.objects.all()[choose].word
    word_sel = [str(word_sel)]

    sentence += word_sel

    pos = floor(rand() * 2)
    if pos == 0:
        getAdjective()
    if pos == 1:
        getNoun()

def getAdjective():
    global sentence
    global adjectives

    nwords = Adjective.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Adjective.objects.all()[choose].word
    word_sel = [str(word_sel)]

    sentence += word_sel

    pos = floor(rand() * 8)
    if pos == 0:
        getAdjective()
    if pos > 0:
        getNoun()

def getNoun():
    global sentence
    global nouns

    nwords = Noun.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Noun.objects.all()[choose].word
    word_sel = [str(word_sel)]

    sentence += word_sel

def getRelativePronoun():
    global sentence
    global pronouns

    nwords = Pronoun.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Pronoun.objects.all()[choose].word
    word_sel = [str(word_sel)]

    sentence += word_sel

def getPreposition():
    global sentence

    nwords = Preposition.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Preposition.objects.all()[choose].word
    word_sel = [str(word_sel)]

    sentence += word_sel

def getVerb():
    global sentence

    nwords = Verb.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Verb.objects.all()[choose].word
    word_sel = [str(word_sel)]

    sentence += word_sel

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

