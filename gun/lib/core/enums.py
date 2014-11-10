#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-

class FingerPrintRules:
    Language_Regex = "x-powered-by:(\S*)\s"
    WebServer_Regex = "server:(\S*)\s"
    From_Regex = "<form.*?action ?= ?\"(.*?)\""
