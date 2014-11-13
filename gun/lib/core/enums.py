#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-


class FingerPrintRules:
    Language_Regex = "x-powered-by:(\S*)\s"
    WebServer_Regex = "server:(\S*)\s"
    From_Regex = "<form.*?action ?= ?\"(.*?)\""
    Title_Regex = "<title>.*</title>"

class CmsFingerPrintRules:
    WordPress_Regex = "<\S* href=\"\S*wp-includes/"