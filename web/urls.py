"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include
from django_nyt.urls import get_pattern as get_nyt_pattern
from wiki.urls import get_pattern as get_wiki_pattern
<<<<<<< HEAD

=======
>>>>>>> 2b5fac999f52516b9071fd5c440dc6da3f5bd39f
# default evennia patterns
from evennia.web.urls import urlpatterns

# eventual custom patterns
custom_patterns = [
<<<<<<< HEAD
    # url(r'/desired/url/', view, name='example'),
     url(r'^notifications/', get_nyt_pattern()),
     url(r'^wiki/', get_wiki_pattern()),
=======
    url(r'^notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern())
>>>>>>> 2b5fac999f52516b9071fd5c440dc6da3f5bd39f
]

# this is required by Django.
urlpatterns = custom_patterns + urlpatterns