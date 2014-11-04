#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

import os
import sys
import sqlite3

class DataHandle(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def connect_db(self):

        conn = sqlite3.connect(self.db_name)

if __name__ == '__main__':
    print os.path.dirname(__file__)
    a={'s':'d'}
    print dict.__init__(a)