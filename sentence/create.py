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

from pablo.sentence.wordStructures import *
#isDjango = False <-- from wordStructures import *

from numpy.random import rand
from numpy import floor

def getSentence():
    ss = Sentence()

    #Obtain the sentence structure
    choose = floor(rand() * 100)
    if choose <= 100:
        VP = getVerbPhrase()
        ss.structure.append(VP)
    
    #Get the word order from the sentence structure
    for structpart in ss.structure:
        ss.words += structpart.words

    #Render the sentence
    for structpart in ss.structure:
        ss.content += structpart.content
               

    if isDjango == False:    
        print '---- STATS ------'
        print 'ss.structure: ', 
        for elem in ss.structure:
            print elem.listStructure(),
        print '\nss.words: ', ss.words
        print 'Number of articles:', ss.words.count('art'), \
            '\tadjectives:', ss.words.count('adj'), \
            '\tnouns:', ss.words.count('noun')
        firstnoun = ss.words.index('noun')
        print 'First Noun:', ss.content[firstnoun]
        print '-----------------'
    
    return ss
        
def getNounPhrase(simple = False):
    NP = NounPhrase()

    #Select the phrase structure
    choose = floor(rand() * 100)
    
    if simple == True:
        #Function call requested a simple NounPhrase
        choose = 0
        
    #Obtain the phrase structure
    if choose < 75:
        NP.structure += getOrnateNoun()
    else:
        NP.structure = getOrnateNoun()     
        NP.structure += getFancyNoun()
    #print 'NP structure: ', NP.listStructure()
        
    #Obtain the words for the Noun Phrase
    for structpart in NP.structure:
        if structpart.type == 'NP':
            NP.words += structpart.words
        else:
            NP.words += [structpart.type]
    #print 'NP.words: ', NP.words
    
    #Render the phrase content
    for structpart in NP.structure:
        if structpart.type == 'NP':
            NP.content += structpart.content
        else:
            NP.content += [structpart.word]
    #print 'NP.content: ', NP.content
    
    NP = NPRules(NP)
    
    return NP

def getFancyNoun():
    choose = floor(rand() * 100)     
    if choose < 50:
        NP = getNounPhrase()
        PRE = getWord('pre')
        structure = [PRE, NP]
    elif choose < 75:
        NP = getNounPhrase()
        PRO = getWord('pro')
        VRB = getWord('vrb')
        structure = [PRO, VRB, NP]
    elif choose < 100:
        NP = getNounPhrase()
        PRO = getWord('pro')
        VRB = getWord('vrb')
        structure = [PRO, NP, VRB]
    
    return structure   


def getOrnateNoun():
    structure = []
    
    choose = floor(rand() * 100)
    if choose < 60:
        ART = getWord('art')
        NOUN = getWord('noun')
        structure += [ART, NOUN] 
    elif choose < 85:
        ART = getWord('art')
        ADJ = getWord('adj')
        NOUN = getWord('noun')
        structure += [ART, ADJ, NOUN]
    elif choose < 97:
        ART = getWord('art')
        ADJ = getWord('adj')
        ADJ2 = getWord('adj')
        NOUN = getWord('noun')
        structure += [ART, ADJ, ADJ2, NOUN]
    elif choose < 100:
        ART = getWord('art')
        ADJ = getWord('adj')
        ADJ2 = getWord('adj')
        ADJ3 = getWord('adj')
        NOUN = getWord('noun')
        structure += [ART, ADJ, ADJ2, ADJ3, NOUN]
        
    return structure
 
def getVerbPhrase():
    VP = VerbPhrase()
        
    #Obtain the phrase structure
    '''
    TODO:   Need more VP structures
         1. NP VRB ON.   e.g. "The cow that jumped over the moon ate the carrot.
         2. ON VRB NP.
    '''

    choose = floor(rand() * 100)
    VP.structure = []
    if choose < 65:
        NP = getNounPhrase()
        VRB = getWord('vrb')
        ON = getNounPhrase(True) 
        VP.structure = [NP, VRB, ON]
    elif choose < 100:
        ON = getNounPhrase(True)
        VRB = getWord('vrb')
        NP = getNounPhrase() 
        VP.structure = [ON, VRB, NP]
     
    #Add an Adverb?
    choose = floor(rand() * 100)
    if choose < 30: 
        #yes! add an adverb!
        ind = VP.structure.index(VRB)
        ADV = getWord('adv')
        VP.structure.insert(ind, ADV)

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
            if ((aa == 'a') or (aa == 'e') or (aa == 'i') or (aa == 'o') or  
                (aa == 'u') or (aa == 'y')):
                NP.content[ind] = 'an'
    
    #TODO: Comma rule
    # Comma structure when Fancy Noun contains Ornate Noun?
      
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
    elif pos == 'adv':
        word_sel = Adverb()    

    else: 
        #Exception -- invalid part of speech
        word_sel = Word()

    word_sel.clean()
    
    return word_sel
