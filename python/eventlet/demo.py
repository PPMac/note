#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eventlet
from eventlet.green import urllib2


urls = [
        "http://www.baidu.com",
        "http://www.163.com",
        "http://www.sina.com.cn/",
       ]


def fetch(url):
    print "Request %s" % url
    return urllib2.urlopen(url).read()

pool = eventlet.GreenPool()
for body in pool.imap(fetch, urls):
    print "Got body", len(body)
