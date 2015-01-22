#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import print_function
from __future__ import unicode_literals
import sys
import os
# hack
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from code.jinja_filters import rfc2822


AUTHOR = 'Henrique Bastos'
SITENAME = 'Curto Circuito Podcast'

SITEURL = 'http://curtocircuito.cc'

RELATIVE_URLS = False

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt'

DELETE_OUTPUT_DIRECTORY = True

PATH = 'content'
STATIC_PATHS = ['images', 'episodes']


# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Generation parameters
DEFAULT_PAGINATION = False

TYPOGRIFY = True

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DIRECT_TEMPLATES = ('index',)

TEMPLATE_PAGES = {'atom.xml': 'atom.xml'}

THEME = "themes/cc"

# Disable:
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''


JINJA_FILTERS = {
    'rfc2822': rfc2822(TIMEZONE),
}


MD_EXTENSIONS = [
    'code.markdown_audio',
    'pyembed.markdown',
    'markdown.extensions.nl2br',
    'markdown.extensions.def_list',
    'markdown.extensions.sane_lists',
]


# Following items are often useful when publishing
DISQUS_SITENAME = "curtocircuitopodcast"
GOOGLE_ANALYTICS = "UA-43277110-1"
TWITTER_USERNAME="curtopodcast"
ITUNES_URL = 'https://itunes.apple.com/us/podcast/curto-circuito-podcast/id712723389'


# Blogroll
"""
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
"""

# Social widget
SOCIAL = (
    ('Facebook', 'http://facebook.com/curtopodcast'),
    ('Twitter', 'http://twitter.com/curtopodcast'),
    ('Google+', 'https://plus.google.com/b/104447350259243628172/104447350259243628172/posts'),
)
