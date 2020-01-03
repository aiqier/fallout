# -*- coding: utf-8 -*-

import nose

from src.dateutil import datetime_to_timestamp_ms
from src.dateutil import datetime_to_timestamp_sec
from src.dateutil import now_datetime

class TestDateUtil(object):

    def test_datetime_to_timestamp_ms(self):
        now = now_datetime()
        print datetime_to_timestamp_ms(now)
        print datetime_to_timestamp_sec(now)