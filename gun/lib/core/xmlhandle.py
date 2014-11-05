#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

import os
import sys
from lxml import etree

class XmlHandle(object):
    def __init__(self, rootNode):
        self.rootNode = etree.Element(rootNode)


    def add_node(self, parentNode, childNode):
        return etree.SubElement(parentNode, childNode)
    def get_node(self, nodeName):
        """
        get node
        :param nodeName:
        :return:
        """
        return self.rootNode.xpath(nodeName)

    def get_nodes_name(self, nodeName):
        """
        get node list
        :param nodeName:
        :return:
        """
        nodes = []
        for i in self.rootNode.xpath(nodeName):
            nodes.append(i)
        return nodes


if __name__ == '__main__':
    pass