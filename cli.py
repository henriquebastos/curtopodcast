#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import click
import eyed3
from eyed3.id3 import ID3_V2_3
from livereload import Server, shell
import re
from unipath import Path

from code.config import ROOT, OUTPUT, CONTENT, EXTENSIONS
from code.entry import next_entry, entry_factory


@click.group()
def cli():
    pass


@cli.command()
@click.argument('port', default=5500, type=int)
def server(port=5500, output=OUTPUT, content=CONTENT, extensions=EXTENSIONS):
    shell('make clean')
    shell('make html')

    output.chdir()
    server = Server()

    cmd = 'pelican -s {} -o {}'.format(ROOT.child('pelicanconf.py'), output)

    for ext in extensions:
        print(content.child(ext))
        server.watch(content.child(ext), cmd)

    print(ROOT.child('themes'))
    server.watch(ROOT.child('themes'), cmd)

    server.watch(output.child('*.html'))
    server.watch(output.child('*.css'))

    server.serve(liveport=35729, port=port)


@cli.command()
@click.argument('title')
@click.option('-e', '--episode', default=next_entry, help='entry title')
@click.option('-a', '--audio', default=None)
def entry(title, episode, audio):
    """
    Creating file-relative-to-cwd.md
    Copying audio to file-relative-to-cwd.mp3
    """
    e = entry_factory(title, episode, audio)

    post_text = CONTENT.child(e.markdown)
    post_audio = CONTENT.child('episodes', e.audio)

    if (not post_text.exists() or
        click.confirm('{} already exists. Override?'.format(post_text), abort=True)):
            click.echo('Writing entry: {}'.format(post_text))
            e.save(post_text)
            click.echo('Done')

    if audio:
        if (not post_audio.exists() or
            click.confirm('{} already exists. Override?'.format(post_audio), abort=True)):
                Path(audio).copy(post_audio)
                click.echo('Done')
        else:
            click.echo('Doing nothing. Entry already exists: {}'.format(post_audio))
    else:
        click.echo('No audio defined.')


@cli.command()
@click.argument('audio', type=click.Path(exists=True, dir_okay=False, resolve_path=True))
@click.option('-e', '--episode', type=int)
@click.option('-t', '--title', required=True)
@click.option('-i', '--image', type=click.Path(exists=True, dir_okay=False, resolve_path=True), help='Image filename for cover art')
def id3(audio, episode, title, image):
    """
    Update ID3 tags with episode info.
    """

    if not episode:  # Try to detect episode from audio filename
        match = re.search(r'e(\d{2,})', audio)
        if not match:
            raise click.UsageError('Could not be detected episode. Use --episode option.')
        episode = int(match.group(1))

    id3 = eyed3.load(audio)

    id3.initTag(version=ID3_V2_3)

    id3.tag.title = title
    id3.tag.artist = 'Henrique Bastos'
    id3.tag.album = 'Curto Circuito Podcast'
    id3.tag.track_num = episode
    id3.tag.genre = 'Podcast'

    if image:
        image = Path(image)
        data = image.read_file('rb')
        mime = 'image/' + image.ext[1:]

        # HACK to make APIC header readable on iTunes
        # EYED3 sets v2.3 encoding to UTF-16, but iTunes only reads LATIN-1
        from eyed3.id3 import frames
        def force_latin1(self):
            self.encoding = eyed3.id3.LATIN1_ENCODING
        setattr(frames.ImageFrame, '_initEncoding', force_latin1)

        # force mime as str because eyeD3 uses it to compose the binary header
        # PUBLISHER_LOGO == 0x14
        id3.tag.images.set(0x14, data, str(mime))

    id3.tag.save(version=ID3_V2_3)

    # Print id3
    shell(['eyeD3', audio])


if __name__ == '__main__':
    cli()