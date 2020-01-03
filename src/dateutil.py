# -*- coding: utf-8 -*-

import datetime
import time

def datetime_to_timestamp_ms(dt):
    """
    date time对象转时间戳(毫秒)
    :return:
    """
    return int(time.mktime(dt.timetuple())) * 1000.0 + dt.microsecond / 1000.0

def datetime_to_timestamp_sec(dt):
    """
    date time对象转时间戳(秒)
    :return:
    """
    return int(time.mktime(dt.timetuple()))


def now_timestamp_ms():
    """
    返回当前时间戳(毫秒)
    :return:
    """
    return datetime_to_timestamp_ms(now_datetime())

def now_timestamp_sec():
    """
    返回当前时间戳(秒)
    :return:
    """
    return datetime_to_timestamp_sec(now_datetime())

def now_datetime():
    """
    返回datetime类型的当前时间
    :return:
    """
    return datetime.datetime.now()