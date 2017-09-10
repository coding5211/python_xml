#!/usr/bin/python3
#encoding=utf-8

import xml.sax
import xml.sax.handler

class WorksHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.names = ""
        self.author = ""
    #元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "works":
            print("***内容***")
            title = attributes["title"]
            print("类型：",title)
    #元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "names":
            print("名称：",self.names)
        elif self.CurrentData == "author":
            print("作者：",self.author)
        self.CurrentData = ""
    #内容事件处理
    def characters(self, content):
        if self.CurrentData == "names":
            self.names = content
        elif self.CurrentData == "author":
            self.author = content

if (__name__ == "__main__"):
    #创建一个XMLReader
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    #重写ContextHandler
    Handler = WorksHandler()
    parser.setContentHandler(Handler)
    parser.parse("works.xml")
