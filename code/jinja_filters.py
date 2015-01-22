# coding: utf-8 
# Jinja Extension
from email import utils
from datetime import datetime
import time
import pytz


def rfc2822(timezone):
    """
    Jinja filter to output date on the format of RFC 2822
    ex: Wed, 03 Dec 2014 11:45:36 -0000
    :param timezone:
    :return: the filter callable
    """
    default_tz = pytz.timezone(timezone)

    def filter(value=None):
        value = value or datetime.today().replace(tzinfo=default_tz)
        t = value.timetuple()
        ts = time.mktime(t)
        return utils.formatdate(ts)

    return filter
