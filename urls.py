from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pablo.views',
    #Django Admin
    (r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Examples:
    # (r'^mysite/', include('mysite.foo.urls')),
    #( r'^polls/', include('mysite.polls.urls')),

    #Core Pablo
    (r'^$', 'index'),

    (r'^store/', 'store'),                      #Save (store) a sentence
    (r'^vote/(?P<sid>\d+)/$', 'vote'),          #Vote for a sentence
    (r'^saved/(?P<sid>\d+)/$', 'saved'),        #Display a stored sentence
    (r'^saved/$', 'savedlist'),			#Display a list of saved sentences

)
