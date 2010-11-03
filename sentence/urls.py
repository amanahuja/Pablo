from django.conf.urls.defaults import *

urlpatterns = patterns('pablo.sentence.views',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    (r'^$', 'index'),
)

