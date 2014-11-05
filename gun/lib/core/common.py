#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-

import os
import re
import sys

from lib.core.data import paths


def banner():
    """
    Banner info
    """
    print 'This is a big gun!!!\r\n'

def setPaths():
    """
    set Environment variable
    :return:
    """
    paths.PAYLOAD_PATH = os.path.join(paths.ROOT_PATH, 'payload')
    paths.TMP_PATH = os.path.join(paths.ROOT_PATH, 'tmp')