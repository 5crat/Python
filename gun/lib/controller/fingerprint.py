#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

from lib.core.data import paths
from lib.core.data import conf
from lib.core.threads import runThreads
from lib.request.httprequest import HttpRequest
from lib.core.xmlhandle import XmlHandle

class FingerPrint(object):
    def __init__(self, target):
        self.target = target

    def discriminate(self):
        pass

    def _read_rules(self):
        pass
