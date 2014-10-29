#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author: xss -*-

import os
import re
import sys
import base64
import argparse
import requests
import threading
from BeautifulSoup import BeautifulSoup

class md5Crack(object):
    def __init__(self, target):
        self.result = []
        self.target = target
        self.headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)'}

    def md5decryption(self):
        url = 'http://md5decryption.com'
        payload = {'hash': self.target, 'submit': 'Decrypt It!'}
        r = requests.post(url, data=payload, headers=self.headers)
        if r.status_code != 200:
            print('[-]'+url+' find error. status code is '+chr(r.status_code))
            return
        soup = BeautifulSoup(r.text)
        data = re.findall("</font></b>(.*)<br", str(soup.findAll('div', attrs={'class': 'main'})[0]))
        if len(data) == 0:
            print('[-]' + url + 5*' ' + 'NotFound')
        else:
            print('[+]' + url + 5*' ' + data[0])

    def md5com(self):
        url = 'http://md5.com.cn'
        url2 = 'http://md5.com.cn/md5reverse'
        headers = self.headers
        headers['Referer'] = url
        r = requests.get(url, headers=self.headers)
        if r.status_code != 200:
            print '[-]'+url+' find error. status code is '+chr(r.status_code)
            return
        soup = BeautifulSoup(r.text)
        sand = soup.find('input', attrs={'type': 'hidden', 'name': 'sand'})['value']
        token = soup.find('input', attrs={'type': 'hidden', 'name': 'token'})['value']
        payload = {'md': self.target, 'sand': str(sand), 'token': str(token), 'submit': 'MD5 Crack'}
        r = requests.post(url2, data=payload, headers=headers)
        try:
            soup = BeautifulSoup(r.text)
            data = re.findall('>(.*)</', str(soup.findAll('span', attrs={'class': 'res green'})[1]))
            if 'NotFound' in str(data[0]):
                print('[-]' + url + 5*' ' + 'NotFound')
            else:
                print('[+]' + url + 5*' ' + data[0])
        except:
            print('[+]' + url + 5*' ' + 'NotFound')
            return

    def md5Rednoize(self):
        url = 'http://md5.rednoize.com/'
        payload = '?p&s=md5&q=' + self.target + '&_='
        headers = self.headers
        headers['Referer'] = url
        headers['X-Requested-With'] = 'XMLHttpRequest'
        r = requests.get(url+payload, headers=headers)
        data = str(r.text)
        if len(data) == 0:
             print('[-]' + url + 5*' ' + 'NotFound')
        else:
            print('[+]' + url + 5*' ' + data)

    def md5im(self):
        url = 'http://md5.im'
        path = '/ajax_crack.php'
        payload = {'hash': self.target}
        headers = self.headers
        headers['Referer'] = url
        headers['X-Requested-With'] = 'XMLHttpRequest'
        r = requests.post(url+path, data=payload, headers=headers)

        try:
            soup = BeautifulSoup(r.text)
            data = soup.find('strong').text
            if self.target == data:
                print(url + 5*' ' + 'NotFound')
            else:
                print('[+]' + url + 5*' ' + data)
        except:
            print('[-]' + url + 5*' ' + 'NotFound')
            return

    def start(self):
        c1 = threading.Thread(target=self.md5im())
        c2 = threading.Thread(target=self.md5decryption())
        c3 = threading.Thread(target=self.md5Rednoize())
        c4 = threading.Thread(target=self.md5com())
        c1.start()
        c2.start()
        c3.start()
        c4.start()

if __name__ == '__main__':
    help = "\r\nUsage:\r\n      md5crack.py strings (16 bit or 32 bit)"
    num = len(sys.argv)
    if num == 2:
        if len(sys.argv[1]) == 16 or len(sys.argv[1]) == 32:
            print('[+] Cracking.......MD5:' + sys.argv[1])
            a = md5Crack(sys.argv[1])
            a.start()
        else:
            print 'MD5 Stings format Error!'
            exit()

    else:
        print help



