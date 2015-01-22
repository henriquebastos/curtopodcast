#!/usr/bin/env python
# coding: utf-8
import click
from livereload import Server, shell
from unipath import Path


ROOT = Path(__file__).parent.absolute()
OUTPUT = ROOT.child('output')
CONTENT = ROOT.child('content')
EXTENSIONS = ('*.md', '*.rst')


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


if __name__ == '__main__':
    cli()