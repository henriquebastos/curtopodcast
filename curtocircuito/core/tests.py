# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from django.conf import settings
from django.contrib.sites.models import Site
from model_mommy.mommy import make as m
from django.core.files import File
from StringIO import StringIO


PUBLISHED = 2


class AtomTest(TestCase):
    def setUp(self):
        s1 = Site.objects.get_current()

        m('Entry', title='T1', status=PUBLISHED, slug='s1', sites=[s1], image=File(StringIO(''), '/i1'))
        m('Entry', title='T2', status=PUBLISHED, slug='s2', sites=[s1], image=File(StringIO(''), '/i2'))
        m('Entry', title='T3', status=PUBLISHED, slug='s3', sites=[s1], image=File(StringIO(''), '/i3'))

        self.resp = self.client.get(r('atom'))

    def test_get(self):
        self.assertContains(self.resp, '<item', 3)

    def test_complete_context(self):
        self.assertNotContains(self.resp, settings.TEMPLATE_STRING_IF_INVALID)

    def test_content_type(self):
        self.assertEqual(self.resp['Content-Type'], 'application/rss+xml')
