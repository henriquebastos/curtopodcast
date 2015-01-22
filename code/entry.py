# coding: utf-8
import re
from datetime import date
from dateutil.relativedelta import relativedelta
from slugify import slugify
from subprocess import check_output, STDOUT
from code.config import CONTENT


TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day}
Summary: {title}
Image: /images/{episode}.jpg
Thumbnail: /images/{episode}.jpg
Audio: /episodes/curtocircuito-{episode}-{title}.mp3
Duration: {hours}:{minutes}:{seconds}
Status: draft

O curto-circuito hoje é ...

[]'s, [HB](http://fb.com/henriquebastos)!

[!audio?type="audio/mpeg"](/episodes/curtocircuito-{episode}-{title}.mp3)

[Download do episódio](/episodes/curtocircuito-{episode}-{title}.mp3)

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

def serial(number):
    """Formated entry serial number used for ordering: e01, e02, ..."""
    return 'e{:0>2}'.format(number)

def entry_date(post):
    """Returns the published date of an entry."""
    with open(post) as f:
        content = f.read()

    m = re.search(r'Date:\s?(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})', content, re.I)
    return date(*[int(i) for i in m.groups()])

def duration(mp3):
    """Return a dict with the episode duration."""
    # TODO: Maybe this should be a timedelta.
    pattern = r'Duration: (?P<hours>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})'
    content = check_output(['ffprobe', '-i', mp3], stderr=STDOUT)
    match = re.search(pattern, content)

    if not match:
        return {}

    return match.groupdict()

def entry(title, mp3):
    entry_date = count_entries(last_entry()) + relativedelta(weeks=+2)

    d = {
        'title': title,
        'slug': slugify(title),
        'episode': serial(count_post() + 1),
        'year': entry_date.year,
        'month': entry_date.month,
        'day': entry_date.day,
    }

    d.update({
        'markdown': '{episode}-{slug}.md'.format(e),
        'audio': 'curtocircuito-{episode}-{slug}.mp3'.format(e),
    })

    d.update(duration(mp3))

    return d
