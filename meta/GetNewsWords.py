import feedparser
import nltk
from collections import defaultdict

#Some userful parameters
nitemstoparse = 5
new_words = []

feedurls = [
  'http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml',
  'http://rss.cnn.com/rss/cnn_topstories.rss',
  ]


'''
1. Get feed contents
  Loop over feedurls to extract and parse content
  Loop over RSS entries in each feed and parse contents
    
'''

for feedurl in feedurls:
  ifeed = feedparser.parse(feedurl)

  for ii in range(nitemstoparse): 
    rssitem = ifeed.entries[ii]

    '''
    2. Parse content to extract entities
    '''
    tokens = nltk.word_tokenize(nltk.clean_html(rssitem.description))
    new_words += tokens


'''
3. Find useful words
We'll prep the word list, remove stopwords and find key words
'''

key_words = [w.lower() for w in new_words if w.isalpha()]
stopwords = nltk.corpus.stopwords.words('english')
key_words = [w for w in key_words if w not in stopwords]

print key_words
print 'Collected {} words, trimmed down to {} key words'.format(len(new_words), len(key_words))
print 'Using {} total articles from {} sources.'.format(nitemstoparse * len(feedurls), len(feedurls))

#most common key words
freqdist = nltk.FreqDist()
for w in key_words: freqdist.inc(w)
print 'Top 10 words by frequency of occurrence are: ', freqdist.keys()[:10]

tag_words = nltk.pos_tag(key_words)

posdict = defaultdict(list)
for k,v in tag_words: posdict[k].append(v)

#print nouns
outfile = open('nouns.txt', 'w')
for noun in posdict['NN']+posdict['NNS']: print>>outfile, noun
outfile.close

'''
Example output: 
 %run news_01.py
 [u'history', u'shows', u'candidates', u'different', u'ways', u'score', u'presidential', u'debates', u'change', u'minds', u'twice', u'debates', u'appeared', u'alter', u'result', u'bo', u'guagua', u'made', u'explicit', u'defense', u'father', u'former', u'communist', u'party', u'official', u'china', u'since', u'sordid', u'political', u'scandal', u'involving', u'entire', u'bo', u'family', u'broke', u'spring', u'two', u'americans', u'three', u'afghans', u'died', u'days', u'pentagon', u'officials', u'confirmed', u'joint', u'operations', u'american', u'afghan', u'forces', u'returning', u'normal', u'fender', u'guitar', u'company', u'made', u'famous', u'likes', u'buddy', u'holly', u'jimi', u'hendrix', u'eric', u'clapton', u'facing', u'big', u'challenges', u'amid', u'fickle', u'tastes', u'wall', u'street', u'music', u'industry', u'fact', u'spanish', u'public', u'pensions', u'limits', u'budget', u'cuts', u'also', u'enhanced', u'reminder', u'one', u'reason', u'europe', u'debt', u'deficit', u'problems', u'proved', u'difficult', u'solve', u'campaigns', u'lowering', u'expectations', u'ahead', u'wednesday', u'first', u'presidential', u'debate', u'two', u'mitt', u'romney', u'notable', u'surrogates', u'raised', u'bar', u'sunday', u'one', u'predicting', u'romney', u'turn', u'race', u'upside', u'bob', u'greene', u'says', u'nixon', u'sweated', u'way', u'tv', u'debate', u'jfk', u'candidates', u'including', u'lbj', u'mcgovern', u'avoided', u'national', u'would', u'fly', u'today', u'chloie', u'leverette', u'gage', u'daniel', u'missing', u'fire', u'burned', u'tennessee', u'home', u'authorities', u'say', u'evidence', u'kids', u'victims', u'blaze', u'least', u'people', u'killed', u'sunday', u'wave', u'bombings', u'iraq', u'making', u'country', u'deadliest', u'day', u'nearly', u'month', u'hours', u'world', u'leaders', u'painted', u'grim', u'picture', u'syrian', u'war', u'new', u'wave', u'attacks', u'erupted', u'today']
 Collected 321 words, trimmed down to 174 key words
 Using 10 total articles from 2 sources.

Now we have a tokenized string from the NYT Global News, ready for Pablo'ifying. 
'''
