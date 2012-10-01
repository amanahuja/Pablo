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

The actual words are fetched from GetWords / getFileWords. 
See the GEB Flowchart for the recursive transition network (RTN) on which the
algorithm is based. 

TODO:
   See Google Doc of Features and Improvements. 

@authors: Aman
'''

from pablo.sentence.WordStructures import *
#isDjango = False <-- from wordStructures import *

from numpy.random import rand
from numpy import floor

#options
show_struct = False

def get_sentence():
    ss = Sentence()

    #Obtain the sentence structure
    choose = floor(rand() * 100)
    if choose <= 100:
        VP = get_verb_phrase()
        ss.structure.append(VP)
    
    #Get the word order from the sentence structure
    for structpart in ss.structure:
        ss.words += structpart.words

    #Render the sentence
    for structpart in ss.structure:
        ss.content += structpart.content
               
    if show_struct == True:    
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
        
def get_noun_phrase(simple = False):
    NP = NounPhrase()

    #Select the phrase structure
    choose = floor(rand() * 100)
    
    if simple == True:
        #Function call requested a simple NounPhrase
        choose = 0
        
    #Obtain the phrase structure
    if choose < 75:
        NP.structure += get_ornate_noun()
    else:
        NP.structure = get_ornate_noun()     
        NP.structure += get_fancy_noun()
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

def get_fancy_noun():
    choose = floor(rand() * 100)     
    if choose < 50:
        NP = get_noun_phrase()
        PRE = get_word('pre')
        structure = [PRE, NP]
    elif choose < 75:
        NP = get_noun_phrase()
        PRO = get_word('pro')
        VRB = get_word('vrb')
        structure = [PRO, VRB, NP]
    elif choose < 100:
        NP = get_noun_phrase()
        PRO = get_word('pro')
        VRB = get_word('vrb')
        structure = [PRO, NP, VRB]
    
    return structure   

def get_ornate_noun():
    structure = []
    
    choose = floor(rand() * 100)
    if choose < 60:
        ART = get_word('art')
        NOUN = get_word('noun')
        structure += [ART, NOUN] 
    elif choose < 85:
        ART = get_word('art')
        ADJ = get_word('adj')
        NOUN = get_word('noun')
        structure += [ART, ADJ, NOUN]
    elif choose < 97:
        ART = get_word('art')
        ADJ = get_word('adj')
        ADJ2 = get_word('adj')
        NOUN = get_word('noun')
        structure += [ART, ADJ, ADJ2, NOUN]
    elif choose < 100:
        ART = get_word('art')
        ADJ = get_word('adj')
        ADJ2 = get_word('adj')
        ADJ3 = get_word('adj')
        NOUN = get_word('noun')
        structure += [ART, ADJ, ADJ2, ADJ3, NOUN]
        
    return structure
 
def get_verb_phrase():
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
        NP = get_noun_phrase()
        VRB = get_word('vrb')
        ON = get_noun_phrase(True) 
        VP.structure = [NP, VRB, ON]
    elif choose < 100:
        ON = get_noun_phrase(True)
        VRB = get_word('vrb')
        NP = get_noun_phrase() 
        VP.structure = [ON, VRB, NP]
     
    #Add an Adverb?
    choose = floor(rand() * 100)
    if choose < 30: 
        #yes! add an adverb!
        ind = VP.structure.index(VRB)
        ADV = get_word('adv')
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
    
def get_word(pos):
    #print 'get_word()'
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
