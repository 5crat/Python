#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-


from libs.plugins.subDomainsBrute.subDomainsBrute import DNSBrute



def getDomainExec(domain, save):
    DNSBrute(domain, output=save).run()
