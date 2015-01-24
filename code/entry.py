# coding: utf-8
from UserDict import UserDict
import re
from datetime import date, time
from subprocess import check_output, STDOUT

from dateutil.relativedelta import relativedelta
from slugify import slugify

from code.config import CONTENT


TEMPLATE = u"""
Title: {title}
Date: {published_at}
Summary: {title}
Image: {image_url}
Thumbnail: {thumbnail_url}
Audio: {audio_url}
Duration: {duration}
Status: draft

O curto-circuito hoje é ...

[]'s, [HB](http://fb.com/henriquebastos)!

[!audio?type="audio/mpeg"]({audio_url})

[Download do episódio]({audio_url})

Edição: [Bruce Bastos](http://brucebastos.com)

**Referências**
- [Description](http://link.com/)

"""


def last_entry(path=CONTENT, pattern='*.md'):
    """Last entry article file."""
    return path.listdir(pattern)[-1]

def count_entries(path=CONTENT, pattern='*.md'):
    """Total of entries."""
    return len(path.listdir(pattern))

def entry_date(post):
    """Returns the published date of an entry."""
    with open(post) as f:
        content = f.read()

    m = re.search(r'Date:\s?(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})', content, re.I)
    return date(*[int(i) for i in m.groups()])


def next_entry(path=CONTENT):
    """Number of the next entry"""
    return count_entries(path) + 1

def next_date(**kwargs):
    """The last entry publication date incremented by kwargs"""
    return (entry_date(last_entry()) + relativedelta(**kwargs)).strftime('%Y-%m-%d')

def serial(number):
    """Formated entry serial number used for ordering: e01, e02, ..."""
    return 'e{:0>2}'.format(number)

def duration(audiofile):
    """Return a time with the episode duration."""
    if not audiofile:
        return ''

    pattern = r'Duration: (?P<hours>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})'
    content = check_output(['ffprobe', '-i', audiofile], stderr=STDOUT)
    match = re.search(pattern, content)

    if not match:
        return ''

    return time(*map(int, match.groups())).strftime('%H:%M:%S')

class Entry(UserDict):
    """Entry object"""
    def __getattr__(self, item):
        return self.data.get(item, '')

    def save(self, filename):
        with open(filename, 'w') as f:
            content = TEMPLATE.strip().format(**self)
            f.write(content.encode('utf-8'))

def entry_factory(title, episode, audio):
    e = Entry({  # Attributes
        'title': title,
        'slug': slugify(title),
        'episode': serial(episode),
        'published_at': next_date(weeks=+2),
        'duration': duration(audio),
    })

    e.update({  # Files
        'markdown': '{episode}-{slug}.md'.format(**e),
        'image': '{episode}.jpg'.format(**e),
        'audio': 'curtocircuito-{episode}-{slug}.mp3'.format(**e),
    })

    e.update({  # Urls
        'image_url': '/images/{image}'.format(**e),
        'thumbnail_url': '/images/{image}'.format(**e),
        'audio_url': '/episodes/{audio}'.format(**e),
    })

    return e