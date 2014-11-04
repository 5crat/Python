#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

import requests


class HttpRequest(object):
    """
        HTTP Request class
    """
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

    def http_request(self):
        """
            HTTP request function
        """
        methods = ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE']
        if self.method.upper() not in methods:
            print r'HTTP请求的方式错误,无法识别该方式： '+ self.method
        r = requests.request(self.method.upper(), self.target, data=self.data, headers=self.headers, proxies=self.proxies)
        header = ''
        for m in r.headers:
            header += m+':'+r.headers[m] + '\r\n'
        return [str(r.status_code), header, r.text]

if __name__ == '__main__':
    a = HttpRequest('http://www.baidu.com', method="post")
    b = a.http_request()
    for i in b:
        print i

