# -*- coding:utf-8 -*-
"""
Created on Nov 13, 2010

@author: Aman
"""

try:    
    isDjango = True
    from pablo.sentence.getWords import *
except ImportError: 
    isDjango = False
    from getFileWords import *

class Sentence:
    def __init__(self): 
        self.structure = []  #Example: [NP, VP]
        self.words = []      #Example: [ART, NOUN, VRB, PREP, ART, ADJ, NOUN]
        self.content = []    #Example: 'the cow sat on the fat frog'

    def listStructure(self):
        ls = ''
        for phrase in self.structure:
            ls += phrase.type + ' '
        return ls

class NounPhrase:
    def __init__(self):
        self.type = 'NP' 
        self.structure = []  #Example: [NP, VP]
        self.words = []      #Example: [ART, NOUN, VRB, PREP, ART, ADJ, NOUN]
        self.content = []    #Example: ['the', 'cow', 'ate', 'a', 'fat', 'frog']
        #self.content = ''    #Example: 'the cow sat on the fat frog'

    def __str__(self):
        return self.type

    def listStructure(self):
        ls = ''
        for phrase in self.structure:
            ls += phrase.type + ' '
        return ls

class VerbPhrase:
    def __init__(self):
        self.type = 'VP' 
        self.structure = []  #Example: [NP, VP]
        self.words = []      #Example: [ART, NOUN, VRB, PREP, ART, ADJ, NOUN]
        self.content = []    #Example: 'the cow sat on the fat frog'

    def __str__(self):
        return self.type

    def listStructure(self):
        ls = ''
        for phrase in self.structure:
            ls += phrase.type + ' '
        return ls

class Word:
    type = ''
    word = ''
    
    def __init__(self):
        self.type = 'Generic'
        self.word = 'Invalid part of speech'
        self.fetch(self)
    
    def clean(self):
        self.word = self.word.replace('\n', '')    
    
    def __str__(self):
        return self.type
        
class Article(Word):
    def __init__(self):
        self.type = 'art'
        self.fetch()
        
    def fetch(self):
        self.word = getArticle()    
    
class Adjective(Word):
    def __init__(self):
        self.type = 'adj'
        self.fetch()
        
    def fetch(self):
        self.word = getAdjective()    

class Noun(Word):
    def __init__(self):
        self.type = 'noun'
        self.fetch()
        
    def fetch(self):
        self.word = getNoun()    

class Verb(Word):
    def __init__(self):
        self.type = 'verb'
        self.fetch()
        
    def fetch(self):
        self.word = getVerb()    

class Preposition(Word):
    def __init__(self):
        self.type = 'prep'
        self.fetch()
        
    def fetch(self):
        self.word = getPreposition()    

class RelPronoun(Word):
    def __init__(self):
        self.type = 'pro'
        self.fetch()
        
    def fetch(self):
        self.word = getRelativePronoun()    

class Adverb(Word):
    def __init__(self):
        self.type = 'adv'
        self.fetch()
        
    def fetch(self):
        self.word = getAdverb()    

