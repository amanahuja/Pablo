# IPython log file

import feedparser
nfeedurl = 'http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml'
get_ipython().magic(u'logstart')
nfeed = feedparser.parse(nfeedurl)
nfeed.popitem()
