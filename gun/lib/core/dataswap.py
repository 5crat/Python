#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-

from Queue import Queue
from lib.core.data import paths
from lib.core.data import conf
from lib.core.xmlhandle import XmlHandle
from lib.core.common import setConfAttribute

def _readXml(filename, node_name, parent_node='', parent_attr=''):
    xdoc = XmlHandle(filepath=paths.PAYLOAD_PATH+filename)
    datas = xdoc.getNodesAttr(node_name, parent_node, parent_attr)
    return datas

conf.fingerprint = Queue()
conf.fingerprint.put('2')
print conf.fingerprint.get()