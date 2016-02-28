#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于进行http请求，以及MD5加密，生成签名的工具类

from __future__ import absolute_import
import httplib
import urllib
import json
import hashlib
import time

def buildMySign(params,secretKey):
    sign = u''
    for key in sorted(params.keys()):
        sign += key + u'=' + unicode(params[key]) +u'&'
    data = sign+u'secret_key='+secretKey
    return  hashlib.md5(data.encode(u"utf8")).hexdigest().upper()

def httpGet(url,resource,params=u''):
    conn = httplib.HTTPSConnection(url, timeout=30)
    conn.request(u"GET",resource + u'?' + params)
    response = conn.getresponse()
    data = response.read().decode(u'utf-8')
    return json.loads(data)

def httpPost(url,resource,params):
     headers = {
            u"Content-type" : u"application/x-www-form-urlencoded",
     }
     print url
     conn = httplib.HTTPSConnection(url, timeout=30)
     temp_params = urllib.urlencode(params)
     conn.request(u"POST", resource, temp_params, headers)
     response = conn.getresponse()
     data = response.read().decode(u'utf-8')
     params.clear()
     conn.close()
     return data


        
     
