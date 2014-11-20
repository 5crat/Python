#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-


import nmap
from lib.core.data import conf
from lib.core.common import setConfAttribute

class PortScanner(object):
    def __init__(self):
        self.target = '127.0.0.1'
        self.nm = nmap.PortScanner()
        self.port = conf.port

    def scanner(self):
        result = {}
        self.nm.scan(self.target, ports=self.port, arguments='-sV')
        print len(self.nm.all_hosts())
        exit()
        for host in self.nm.all_hosts():
            result['host'] = host
            result['state'] = self.nm[host].state()
            '''
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, self.nm[host].hostname()))
            print('State : %s' % self.nm[host].state())
            '''
            for proto in self.nm[host].all_protocols():
                if proto not in ['tcp', 'udp']:
                    continue
                print('----------')
                print('Protocol : %s' % proto)
                lport = self.nm[host][proto].keys()
                lport.sort()
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, self.nm[host][proto][port]['state']))


if __name__ == '__main__':
    setConfAttribute()
    conf.target = '127.0.0.1'
    conf.port = None
    a = PortScanner()
    a.scanner()