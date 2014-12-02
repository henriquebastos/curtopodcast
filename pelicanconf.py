#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.markdown import PyEmbedMarkdown
from markdown.extensions.nl2br import Nl2BrExtension


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

THEME = "themes/cc"

ITUNES_URL = 'https://itunes.apple.com/us/podcast/curto-circuito-podcast/id712723389'


from markdown.inlinepatterns import Pattern
from markdown import Extension

class AudioPattern(Pattern):
    PATTERN = '\[!audio(\?(?P<attr>.*))?\]\((?P<url>.*)\)'

    def __init__(self, md):
        super(AudioPattern, self).__init__(self.PATTERN)

        self.md = md

    def handleMatch(self, m):
        params = m.groupdict()
        print(params)
        html = '<audio controls=""><source src="{url}" {attr}">Seu browser não suporta a tag de audio HTML5.</audio>'.format(**params)

        return self.md.htmlStash.store(html)

class AudioMarkdown(Extension):
    def __init__(self, renderer=None):
        super(AudioMarkdown, self).__init__()
        self.renderer = renderer

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add(
            'audio', AudioPattern(md), '_begin')

MD_EXTENSIONS = [PyEmbedMarkdown(), Nl2BrExtension(), AudioMarkdown(), 'markdown.extensions.def_list', 'markdown.extensions.sane_lists']

