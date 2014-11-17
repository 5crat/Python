#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-

import MySQLdb

class DB(object):


    def __init__(self, dbname, username, password, host='localhost', port='3306'):
        self.dbname = dbname
        self.username = username
        self.password = password
        self.host = host
        self.port = port

        self.conn = MySQLdb.connect(
            dbname=self.dbname,
            user=self.username,
            passwd=self.password,
            host=self.host,
            port=self.port,
            )
        self.cur = self.conn.cursor()

    def select(self):
        self.cur.execute("")