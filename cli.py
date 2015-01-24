#!/usr/bin/env python
# coding: utf-8
import click
from livereload import Server, shell
from code.config import ROOT, OUTPUT, CONTENT, EXTENSIONS
from code.entry import next_entry, entry_factory


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




if __name__ == '__main__':
    cli()