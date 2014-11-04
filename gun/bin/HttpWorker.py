#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

import requests


#    HTTP工作类

class HttpWorker(object):
    '''
        构造函数，初始化请求目标，请求模式，以及POST的数据
    '''
    def __init__(
            self,
            target,
            method='GET',
            data='',
            proxies='',
            useragent='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
    ):
        self.target = target
        self.method = method
        self.data = data
        self.proxies = proxies
        self.UserAgent = useragent
        self.headers = {
            'User-Agent': self.UserAgent,
            'Referer': target
        }

    '''
        HTTP请求方法
    '''
    def http_request(self):
        methods = ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE']
        if self.method.upper() not in methods:
            print r'HTTP请求的方式错误,无法识别该方式： '+ self.method
        r = requests.request(self.method.upper(), self.target, data=self.data, headers=self.headers, proxies=self.proxies)
        header = ''
        for m in r.headers:
            header += m+':'+r.headers[m] + '\r\n'
        return [str(r.status_code), header, r.text]

if __name__ == '__main__':
    a = HttpWorker('http://www.baidu.com', method="post")
    b = a.http_request()
    for i in b:
        print i

