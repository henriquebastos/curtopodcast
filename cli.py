#!/usr/bin/env python
# coding: utf-8
import click
from livereload import Server, shell
from code.config import ROOT, OUTPUT, CONTENT, EXTENSIONS
from code.entry import entry, TEMPLATE


@click.group()
def cli():
    pass


@cli.command()
@click.option('port', default=5500, type=int, help='wsgi server port')
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
@click.option('title', help='entry title')
@click.option('audio', help='entry audio file')
def make_entry(title, mp3):
    assert title and mp3.exists(), 'Title and Episode file must be informed'

    e = entry(title, mp3)

    text = CONTENT.child(e['markdown'])
    audio = CONTENT.child('episodes', e['audio'])

    if not text.exists():
        text.write_file(TEMPLATE.strip().format(e))
    else:
        print('Doing nothing. File already exists: {}'.format(text))


    if not audio.exists():
        mp3.copy(audio)
    else:
        print('Doing nothing. Entry already exists: {}'.format(audio))


if __name__ == '__main__':
    cli()