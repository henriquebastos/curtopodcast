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
