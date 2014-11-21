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
        for host in self.nm.all_hosts():
            result[host] = {}
            result[host]['state'] = self.nm[host].state()
            '''
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, self.nm[host].hostname()))
            print('State : %s' % self.nm[host].state())
            '''
            for proto in self.nm[host].all_protocols():
                if proto not in ['tcp', 'udp']:
                    continue
                '''
                print('----------')
                print('Protocol : %s' % proto)
                '''
                lport = self.nm[host][proto].keys()
                lport.sort()
                p = []
                for port in lport:
                    m = self.nm[host][proto]
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


if __name__ == '__main__':
    setConfAttribute()
    conf.target = '127.0.0.1'
    conf.port = None
    a = PortScanner()
    print a.scanner()