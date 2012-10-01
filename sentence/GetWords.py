# -*- coding:utf-8 -*-
"""
Created on Nov 1, 2010

This package fetches words for Django based environments containing
word lists in a sqlite database. 

@author: Aman
"""

from numpy.random import rand
from numpy import floor
import warnings

from pablo.sentence.models import *
from pablo.HelperFunctions import format_warning

warnings.formatwarning = format_warning

def get_article():
    nwords = Article.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Article.objects.all()[choose].word
    word_sel = str(word_sel)    
    return word_sel
    
def get_adjective():
    nwords = Adjective.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Adjective.objects.all()[choose].word
    word_sel = str(word_sel)
    return word_sel

def get_noun():
    useFile = int(floor(rand() * 2))

    if useFile == 1:
      wfile = open('pos/nouns.txt', 'r')
      filewords = wfile.readlines()
      wfile.close()

      nwords = len(filewords)
      choose = int(floor(rand() * nwords))
      word_sel = filewords[choose]
      warnings.warn('Using word from file: {}.'.format(word_sel))

    else:
      nwords = Noun.objects.count()
      choose = int(floor(rand() * nwords))
      word_sel = Noun.objects.all()[choose].word
      word_sel = str(word_sel)

    return word_sel

def get_relative_pronoun():    
    nwords = Pronoun.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Pronoun.objects.all()[choose].word
    word_sel = str(word_sel)
    return word_sel

def get_preposition():
    nwords = Preposition.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Preposition.objects.all()[choose].word
    word_sel = str(word_sel)
    return word_sel

def get_verb():
    nwords = Verb.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Verb.objects.all()[choose].word
    word_sel = str(word_sel)
    return word_sel

def get_adverb():
    nwords = Adverb.objects.count()
    choose = int(floor(rand() * nwords))
    word_sel = Adverb.objects.all()[choose].word
    word_sel = str(word_sel)
    return word_sel

def format_string(sentence):
    ss = ''
    for ii in range(len(sentence)):
        ss += sentence[ii]
        ss += ' '
    ss = ss.replace('\n', '')
    ss = ss.capitalize()
    ss = ss.strip()
    ss += '.'
    return ss
