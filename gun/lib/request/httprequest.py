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
            target='',
            web_method='GET',
            data='',
            proxies='',
            timeout=5,
            useragent='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
    ):
        self.target = target
        self.web_method = web_method
        self.data = data
        self.proxies = proxies
        self.timeout = timeout
        self.UserAgent = useragent
        self.headers = {
            'User-Agent': self.UserAgent,
            'Referer': self.target
        }

    def http_request(self):
        """
        http request method
        :return list {'status_code':...,''header:....,'content':...}
        """
        try:
            if not self.target:
                return
            methods = ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE']
            if self.web_method.upper() not in methods:
                print r'HTTP请求的方式错误,无法识别该方式： '+ self.method
            r = requests.request(self.web_method.upper(), self.target, data=self.data, headers=self.headers,\
                                 proxies=self.proxies, timeout=self.timeout)
            headers = {}
            for m in r.headers:
                headers[m] = r.headers[m]
            return {'status_code': str(r.status_code), 'header': headers, 'content':  r.text}
        except:
            return None

if __name__ == '__main__':
    a = HttpRequest('http://www.baidu.com', web_method="post")
    b = a.http_request()
    for i in b:
        print b[i]

