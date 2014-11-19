#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

import re
from lib.core.data import conf
from lib.core.data import paths
from lib.core.enums import FingerPrintRules
from lib.core.common import setConfAttribute
from lib.controller.wappalyzer import Wappalyzer


def check_fingerprint():
    result = Wappalyzer(datafile_path='../../payload/apps.json').analyze()
    if result['status_code'] == '200':
        headers = ''
        for i in result['headers']:
            headers += i + ':' + result['headers'][i] + '\r\n'
        content = result['html'].lower()
        tmp_language = re.findall(FingerPrintRules.LanguageRegex, headers.lower())
        tmp_form = re.findall(FingerPrintRules.FromRegex, content)
        tmp_title = re.findall(FingerPrintRules.TitleRegex, content)
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
        else:
            result['server'] = 'UnKnown'
    return result

if __name__ == '__main__':
    setConfAttribute()
    conf.target = 'http://cn.wordpress.org/'
    conf.web_method = 'GET'
    conf.timeout = 2
    data = check_fingerprint()
    print data['web-servers']
    print data['language']
    print data['cms']