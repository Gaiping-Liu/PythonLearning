#!/usr/bin/env pathon3
# _*_ coding: utf-8 _*_
# Author: Gaiping Liu gaipingliu@outlook.com

#import urllib.request
#import urllib.parse
import socket
import urllib.error
from urllib import request, parse
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
from http import cookiejar

def baseTest():
    res = urllib.request.urlopen('https://www.python.org')
    print(res.status, res.getheaders(), res.getheader('Server'))
    #print(response.read().decode('utf-8'))

#test data para with urlopen method
def testData():
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
    re2 = urllib.request.urlopen('http://httpbin.org/post', data=data)
    print(re2.read())

#test timeout
def testTimeOut():
    try:
        resp = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('time out')
        
def testRequest():
    req = urllib.request.Request('http://python.org')
    resp = urllib.request.urlopen(req)
    print(resp.read().decode('utf-8'))

def testHearder():
    url='http://httpbin.org/post'
    headers={
        'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host' : 'httpbin.org'
    }
    dic = {
        'name' : 'Germey'
    }
    data = bytes(parse.urlencode(dic), encoding='utf-8')
    req= request.Request(url=url, data=data, headers=headers,method='POST')
    resp = request.urlopen(req)
    print(resp.read().decode('utf-8'))
    
def testPassWord():
    username = 'username'
    password = 'password'
    url = 'http://localhost:5000/'
    
    p= HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    auth_handler = HTTPBasicAuthHandler(p)
    opener = build_opener(auth_handler)
    
    try:
        result = opener.open(url)
        html = result.read().decode('utf-8')
        print(html)
    except URLError as e:
        print(e.reason)

def testCookies():
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = build_opener(handler)
    res = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + "=" + item.value)

#testPassWord()

testCookies()