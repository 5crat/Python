#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

import re
from lib.core.data import conf
from lib.core.enums import FingerPrintRules
from lib.core.common import setConfAttribute
from lib.request.httprequest import HttpRequest


class WebFingerPrint(HttpRequest):
    def __init__(self):
        HttpRequest.__init__(self)
        self.target = conf.target
        self.web_method = conf.web_method
        self.data = conf.data
        self.headers = conf.headers
        self.proxies = conf.proxies
        self.UserAgent = conf.useragent
        self.timeout = conf.timeout

    def _get_response(self):
        """
        get http response data
        :return  {'status_code': .., 'header': .., 'content': ..}:
        """
        response_data = HttpRequest.http_request(self)
        return response_data

    def check_fingerprint(self):
        data = self._get_response()
        result = {}
        if data['status_code'] == '200':
            header = data['header'].lower()
            content = data['content'].lower()
            tmp_language = re.findall(FingerPrintRules.Language_Regex, header)[0]
            tmp_server = re.findall(FingerPrintRules.WebServer_Regex, header)[0]
            tmp_form = re.findall(FingerPrintRules.From_Regex, content)[0]
            tmp_title = re.findall(FingerPrintRules.Title_Regex, content)[0]
            result['title'] = tmp_title
            if tmp_form:
                if '.php' in tmp_form:
                    result['language'] = 'php'
                elif '.asp' in tmp_form or '.aspx' in tmp_form:
                    result['language'] = 'asp'
                elif '.jsp' in tmp_form or '.do' in tmp_form or '.action' in tmp_form:
                    result['language'] = 'jsp'
                else:
                    result['language'] = 'UnKnown'
            else:
                result['language'] = 'UnKnown'
            if result['language'] == 'UnKnown':
                if tmp_language:
                    if 'php' in tmp_language:
                        result['language'] = tmp_language
                    elif 'asp' in tmp_language:
                        result['language'] = tmp_language
                    elif 'jsp' in tmp_language or 'servlet' in tmp_language:
                        result['language'] = tmp_language
                    else:
                        result['language'] = 'UnKnown'
            if tmp_server:
                result['server'] = tmp_server
                if result['language'] == 'UnKnown':
                    if 'tomcat' in tmp_server:
                        result['language'] = 'jsp'
                    elif 'nginx' in tmp_server or 'apache' in tmp_server:
                        result['language'] = 'php'
                    elif 'iis' in tmp_server:
                        result['language'] = 'asp'
            else:
                result['server'] = 'UnKnown'
        return result

if __name__ == '__main__':
    setConfAttribute()
    conf.target = 'http://42.192.0.3:8080/'
    conf.web_method = 'GET'
    conf.timeout = 2
    a = WebFingerPrint()
    data = a.check_fingerprint()
    print data['language']
    print data['server']
