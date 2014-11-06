#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-

import os
import re
import sys

from lib.core.data import paths
from lib.core.data import conf


def init():
    _setPaths()
    _setConfAttribute()
def banner():
    """
    Banner info
    """
    print 'This is a big gun!!!\r\n'

def _setPaths():
    """
    set Environment variable
    :return:
    """
    paths.PAYLOAD_PATH = os.path.join(paths.ROOT_PATH, "payload")
    paths.TMP_PATH = os.path.join(paths.ROOT_PATH, "tmp")

def _setConfAttribute():
    conf.url = None
    conf.ip = None
    conf.port = None
    conf.cookie = None
    conf.useragent = None
    conf.proxylist = []