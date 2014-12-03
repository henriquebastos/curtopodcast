#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Henrique Bastos'
SITENAME = 'Curto Circuito Podcast'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'episodes']

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Facebook', 'http://facebook.com/curtopodcast'),
    ('Twitter', 'http://twitter.com/curtopodcast'),
    ('Google+', 'https://plus.google.com/b/104447350259243628172/104447350259243628172/posts'),
)

TWITTER_USERNAME="curtopodcast"

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TYPOGRIFY = True

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

DIRECT_TEMPLATES = ('index',)

TEMPLATE_PAGES = {'atom.xml': 'atom.xml'}

THEME = "themes/cc"

ITUNES_URL = 'https://itunes.apple.com/us/podcast/curto-circuito-podcast/id712723389'

from datetime import datetime
import pytz

def isoformat(value):
    value = value or datetime.today().replace(tzinfo=pytz.timezone(TIMEZONE))
    return value.isoformat()

JINJA_FILTERS = {
    'isoformat': isoformat,
}


MD_EXTENSIONS = [
    'markdown_audio',
    'pyembed.markdown',
    'markdown.extensions.nl2br',
    'markdown.extensions.def_list',
    'markdown.extensions.sane_lists',
]





