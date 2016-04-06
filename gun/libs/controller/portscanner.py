#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-


import nmap
from libs.core.data import conf
from libs.core.common import setConfAttribute
from Queue import Queue
import MySQLdb
from libs.core.setting import DB
from libs.core.data import logger


def connectdb():
    dbname = DB['dbname']
    username = DB['username']
    password = DB['password']
    host = DB['host']
    port = DB['port']

    conn = MySQLdb.connect(
        db=dbname,
        user=username,
        passwd=password,
        host=host,
        port=port,
        charset='utf8',
        )
    return conn

def readTarget(conn):
    resultQueue = Queue()
    cur = conn.cursor()
    cur.execute("select id,ip from host")
    results = cur.fetchall()
    for target in results:
        resultQueue.put(target)
    return resultQueue


def port_scanner(target, ports=None):
    result = {}
    target = target
    nm = nmap.PortScanner()
    port = ports
    if port == None:
        nm.scan(target, arguments='-sV -Pn')
    else:
        nm.scan(target, ports=port, arguments='-sV -Pn')
    for host in nm.all_hosts():
        result[host] = {}
        result[host]['state'] = nm[host].state()
        '''
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, self.nm[host].hostname()))
        print('State : %s' % self.nm[host].state())
        '''
        for proto in nm[host].all_protocols():
            if proto not in ['tcp', 'udp']:
                continue
            '''
            print('----------')
            print('Protocol : %s' % proto)
            '''
            lport = nm[host][proto].keys()
            lport.sort()
            p = []
            for port in lport:
                m = nm[host][proto]
                p.append(
                    {
                        port: m[port]['state'],
                        'name': m[port]['product'],
                        'service': m[port]['name'],
                        'version': m[port]['version'],
                        'cpe': m[port]['cpe']
                    }
                )
                #print ('port : %s\tstate : %s' % (port, self.nm[host][proto][port]['state']))
            result[host]['port'] = p
    return result


def writedb(conn, ports, ID):
    try:
        cur = conn.cursor()
        cur.execute("update host set port='"+ports+"' where id="+ID)
        conn.commit()
    except Exception as e:
        logger.warning(e)
        return

if __name__ == '__main__':
    conn = connectdb()
    tasks = readTarget(conn)
    while tasks.empty() == False:
        target = tasks.get()
        Id = target[0]
        ip = target[1]
        try:
            b = port_scanner(ip)
            result = b[ip]['port']
        except Exception as e:
            #print "Error" + str(Id)
            logger.warning(e)
            continue
        print result
        ports = ''
        for i in result:
            for l in i.keys():
                if isinstance(l, int):
                    if i[l] == 'open':
                        ports += str(l) + ','
        ports = ports.rstrip(',')
        writedb(conn, ports, str(Id))
    conn.close()