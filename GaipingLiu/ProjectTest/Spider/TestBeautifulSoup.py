#!/usr/bin/env pathon3
# _*_ coding: utf-8 _*_
# Author: Gaiping Liu gaipingliu@outlook.com

from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
import bs4

def get_baidu_news(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
            
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def baiduNews():
    url='http://news.baidu.com/'
    html=get_baidu_news(url)
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title.string)
    for a in soup.find_all(name='a'):
        if a.attrs.get('href') != None:
            if a['href'] != '' and a.string != None and a.string != '':
                print(a.string)

def marc():
    url='https://marc.info/?l=aic7xxx&m=138098284729110&w=2'
    html = get_baidu_news(url)
    soup = BeautifulSoup(html, 'lxml')
    target =soup.find(name='pre')#, recursive=False)
    if  target != None:
        for item in target.contents:
            if type(item) is bs4.element.NavigableString and item.strip().replace('\n','') != '':
                print(item)
                print(type(item))
            

#baiduNews()
marc()