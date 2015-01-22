# coding: utf-8
from unipath import Path


ROOT = Path(__file__).parent.parent.absolute()
OUTPUT = ROOT.child('output')
CONTENT = ROOT.child('content')
EXTENSIONS = ('*.md', '*.rst')
