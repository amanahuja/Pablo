# -*- coding:utf-8 -*-
'''
Created on Oct 04, 2010 @Aman
   Last modified Nov 15th @Aman
    
These functions assemble sentence phrases and sentences. Rules are then applied
to each assembly. Assembly and the application of rules are performed on 
several levels: 
    * Sentence
    * Phrase
    * Word

The actual words are fetched from getWords / getFileWords. 
See the GEB Flowchart for the recursive transition network (RTN) on which the
algorithm is based. 

TODO:
   See Google Doc of Features and Improvements. 

@authors: Aman
'''

#Import Word Lists from Django if available, else use test lists.
isDjango = True
try:    
    from pablo.sentence.wordStructures import *
except ImportError: 
    isDjango = False
    from wordStructures import *

#Import numpy or pylab, as available. 
try: 
    from numpy.random import rand
    from numpy import floor
except ImportError:
    from pylab import rand, floor

def getSentence():
    ss = Sentence()

    #Obtain the sentence structure
    choose = floor(rand() * 100)
    if choose < 70:
        NP = getNounPhrase()
        ss.structure.append(NP)
        VP = getVerbPhrase()
        ss.structure.append(VP)
    elif choose <= 100:
        NP = getNounPhrase()
        ss.structure.append(NP)
    
    #Get the word order from the sentence structure
    for structpart in ss.structure:
        ss.words += structpart.words

    #Render the sentence
    for structpart in ss.structure:
        ss.content += structpart.content
               

    if isDjango == False:    
        print '---- STATS ------'
        print 'ss.structure: ', ss.listStructure()
        print 'ss.words: ', ss.words
        print 'Number of articles:', ss.words.count('art'), \
            '\tadjectives:', ss.words.count('adj'), \
            '\tnouns:', ss.words.count('noun')
        firstnoun = ss.words.index('noun')
        print 'First Noun:', ss.content[firstnoun]
        print '-----------------'
    
    return ss

def getNounPhrase():
    NP = NounPhrase()

    #Obtain the phrase structure
    choose = floor(rand() * 100)
    if choose < 40:
        ART = getWord('art')
        NOUN = getWord('noun')
        NP.structure += [ART, NOUN] 
    elif choose < 70:
        ART = getWord('art')
        ADJ = getWord('adj')
        NOUN = getWord('noun')
        NP.structure += [ART, ADJ, NOUN]
    elif choose < 90:
        ART = getWord('art')
        ADJ = getWord('adj')
        ADJ2 = getWord('adj')
        NOUN = getWord('noun')
        NP.structure += [ART, ADJ, ADJ2, NOUN]
    elif choose < 100:
        ART = getWord('art')
        ADJ = getWord('adj')
        ADJ2 = getWord('adj')
        ADJ3 = getWord('adj')
        NOUN = getWord('noun')
        NP.structure += [ART, ADJ, ADJ2, ADJ3, NOUN]
    #print 'NP structure: ', NP.listStructure()
    
    #Obtain the words for the Noun Phrase
    for structpart in NP.structure:
        NP.words += [structpart.type]
    #print 'NP.words: ', NP.words
    
    #Render the phrase content
    for structpart in NP.structure:
        NP.content += [structpart.word]    
    #print 'NP.content: ', NP.content
    
    NP = NPRules(NP)
    
    return NP

def getVerbPhrase():
    VP = VerbPhrase()

    #Obtain the phrase structure
    choose = floor(rand() * 100)     
    if choose < 25:
        NP = getNounPhrase()
        PRE = getWord('pre')
        VP.structure = [PRE, NP]
    elif choose < 50:
        NP = getNounPhrase()
        PRO = getWord('pro')
        VRB = getWord('vrb')
        VP.structure = [PRO, VRB, NP]
    elif choose < 100:
        NP = getNounPhrase()
        PRO = getWord('pro')
        VRB = getWord('vrb')
        VP.structure = [PRO, NP, VRB]
    #print 'VP structure: ', VP.listStructure()
     
    #Obtain the words for the Verbphrase
    for structpart in VP.structure:
        if structpart.type == 'NP':
            VP.words += structpart.words
        else:
            VP.words += [structpart.type]
    #print 'VP words:', VP.words
   
    #Render the phrase content
    for structpart in VP.structure:        
        if structpart.type == 'NP':
            VP.content += structpart.content
        else:
            VP.content += [structpart.word]
    #print 'VP content:' , VP.content
    
    return VP

def NPRules(NP):

    #Indef article 'a' --> 'an'
    if NP.words.index('art') >= 0:
        ind = NP.words.index('art')
        if NP.content[ind] == 'a':
            aa = NP.content[ind+1][0]
            if (aa == 'a') or (aa == 'e') or (aa == 'i') or (aa == 'o') or (aa == 'u') or (aa == 'y'):
                NP.content[ind] = 'an'
        
    return NP
    
def getWord(pos):
    #print 'getWord()'
    if pos == 'art': 
        word_sel = Article()
    elif pos == 'adj':
        word_sel = Adjective()
    elif pos == 'noun': 
        word_sel = Noun()
    elif pos == 'vrb': 
        word_sel = Verb()
    elif pos == 'pre':
        word_sel = Preposition()
    elif pos == 'pro':
        word_sel = RelPronoun()
        
    else: 
        #Exception -- invalid part of speech
        word_sel = Word()

    word_sel.clean()
    
    return word_sel
