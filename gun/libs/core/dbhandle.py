#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-

import MySQLdb
from libs.core.setting import DB
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

    def executeSql(self, sql, data):
        try:
            if data:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, data)
            return self.cur
        except:
            return None

    def insert(self, tableName, dataDict):
        """
        :type tableName:str
        :type dataDict:dict
        :return :bool
        """
        sql = "INSERT INTO "+tableName+" ("
        for i in dataDict.keys():
            sql += i + ','
        sign = len(dataDict) * "%s"
        sql = sql.rstrip(',') + ") VALUES (" + sign.replace('%s', '%s,').rstrip(',') +")"
        if self.executeSql(sql, dataDict.values()):
            return True
        else:
            return False

    def close(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()
'''
    def select(self):
        self.cur.execute("select * from ")
'''

if __name__ == '__main__':
    '''
    d = DBhandle()
    f = d.execute('select * from bank where bank_id=1')
    for i in f:
        print i
    d.close()
        '''
    dataDict= {'a':'a','b':'a'}
    tableName = 'xxx'

    sql = "INSERT INTO "+tableName+" ("
    for i in dataDict.keys():
        sql += i+','

    sign = len(dataDict) * "%s"
    sql = sql.rstrip(',') + ") VALUES (" + sign.replace('%s', '%s,').rstrip(',') +")"
    print sql