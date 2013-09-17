# Create your views here.
from django.shortcuts import render
import pytz
from django.utils.datetime_safe import datetime
from zinnia.models import Entry


def atom(request):
    context = dict(
        lastBuildDate=datetime.utcnow().replace(tzinfo=pytz.utc),
        entries=Entry.published.all(),
    )
    return render(request, 'atom.xml', context, content_type='text/xml')
