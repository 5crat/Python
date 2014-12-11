#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-

import MySQLdb
from lib.core.setting import DB
class DBhandle(object):

    def __init__(self):
        self.dbname = DB['dbname']
        self.username = DB['username']
        self.password = DB['password']
        self.host = DB['host']
        self.port = DB['port']

        self.conn = MySQLdb.connect(
            db=self.dbname,
            user=self.username,
            passwd=self.password,
            host=self.host,
            port=self.port,
            charset='utf8',
            )
        self.cur = self.conn.cursor()

    def execute(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur
        except:
            return None
    def close(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()
'''
    def select(self):
        self.cur.execute("select * from ")
'''

if __name__ == '__main__':
    d = DBhandle()
    f = d.execute('select * from bank where bank_id=1')
    for i in f:
        print i
    d.close()