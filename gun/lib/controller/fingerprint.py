#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

from lib.core.data import conf
from lib.core.common import _setConfAttribute
from lib.request.httprequest import HttpRequest

class FingerPrint(HttpRequest):
    def __init__(self):
        self.target = conf.target
        self.method = conf.method
        self.data = conf.data
        self.headers = conf.headers
        self.proxies = conf.proxies
        self.UserAgent = conf.useragent
        self.timeout = conf.timeout

if __name__ == '__main__':
    _setConfAttribute()
    conf.target = 'http://www.badboydiary.com/'
    conf.method = 'GET'
    conf.timeout = 2
    a = FingerPrint()
    b = a.http_request()
    for i in b:
        print i