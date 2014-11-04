#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

import re
import requests
from HttpWorker import HttpWorker
from scrapy.spider import BaseSpider
from BeautifulSoup import BeautifulSoup
from scrapy.utils.url import urljoin_rfc
from scrapy.selector import HtmlXPathSelector


class FingerPrint(object):
    def __init__(self, target):
        self.target = target

    def discriminate(self):
        pass

    def _read_rules(self):
        pass
