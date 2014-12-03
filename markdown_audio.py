# coding: utf-8
"""
Markdown extension for HTML5 audio tag.

Usages:
[!audio](http://domain.com/my.mp3)
[!audio?type="audio/mpeg"](http://domain.com/my.mp3)

Install it on Pelican's config file:

MD_EXTENSIONS = ['markdown_audio']
"""
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


def makeExtension(*args, **kwargs):
    return AudioMarkdown(*args, **kwargs)
