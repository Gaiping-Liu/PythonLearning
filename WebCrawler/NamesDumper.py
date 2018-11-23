#!/usr/bin/env python
#encoding: utf-8  


import requests
import bs4
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import os
from threading import Thread
import threading
import re
import time
import urllib
import urllib.request
import random

file_lock = threading.Lock()
i =0
user_agent = 'Mozilla/5.0(X11;Ubuntu;Linux x86_64;rv:32.0)Gecko/20100101 Firefox/32.0'
headers = {'User-Agent':user_agent}

def extract_contents(keyword, outputPath):
    
    try: # get URl content
        temp = urllib.request.quote(keyword)
        if temp == keyword:
            Url = "https://www.names.org/n/"+urllib.request.quote(temp)+"/about"
            req = urllib.request.Request(Url,headers = headers)
            Res = urllib.request.urlopen(req)
            ResultPage =  Res.read().decode("utf-8")
            soup = BeautifulSoup(ResultPage,"html.parser")
            firstnameCount, lastnameCount, origin =None, None, None

            #get last name count
            lastnameCount = soup.find(name ='div', attrs ={'class':'popularity-box last-name'})
            if lastnameCount != None:
                lastnameCount= lastnameCount.find(name = 'span', attrs ={'class':'number'})
                if lastnameCount != None:
                    lastnameCount= lastnameCount.get_text()

            #get origin
            origin = soup.find(name ='ul', attrs ={'class':'list-inline quick-facts'})
            if origin != None:
                for node in origin.find_all(name='li'):
                    text = node.get_text()
                    if 'Origin' in text:
                        origin = text.strip().replace('\t', '').replace('\n', '').replace('Origin:', '')
                        break

                #origin = origin.find(name='li', text=re.compile('Origin'))
                #if origin!=None:
                #    temp= origin.find(name='a')
                #    if temp!=None:
                #        origin = temp.get_text()
                #    else:
                #        origin = origin.get_text()

            #get first name count
            firstnameCount = soup.find(name ='div', attrs ={ 'class':'popularity-box gender-boy'})
            if firstnameCount != None:
                firstnameCount = firstnameCount.find(name = 'span', attrs ={'class':'number'})
                if firstnameCount != None:
                    firstnameCount= firstnameCount.get_text() #name-box-left > div > div.popularity-box.gender-boy
            else:
                firstnameCount = soup.find(name ='div', attrs ={'class':'popularity-box gender-girl'})
                if firstnameCount != None:
                    firstnameCount = firstnameCount.find(name = 'span', attrs ={'class':'number'})
                    if firstnameCount != None:
                        firstnameCount= firstnameCount.get_text()
            
            outline = keyword + '\t' + str(firstnameCount) + '\t' + str(lastnameCount)+'\t'+str(origin)
            if(file_lock.acquire(True)):
                with open(outputPath, 'a+', encoding='utf-8') as wf:
                    outline = outline + '\n'
                    wf.write(outline)
                    #i = i+1
                    #print(i)
                file_lock.release()
    except Exception as e:
        print("error")
        return ''

def process_all_file():
    with open(r'E:\Frontend\en-US\Outlook\PersonNameDump\namesorg\testNew\test.txt','r', encoding='utf-8') as rf:
        allLines= rf.readlines()
        
    outputPath = r'E:\Frontend\en-US\Outlook\PersonNameDump\namesorg\testNew\test.result.txt'
    for line in allLines:
        temp = line.strip()
        if temp != '':
            extract_contents(temp, outputPath)
            #Thread(target = extract_contents, args = (line.strip(), outputPath)).start()
        time.sleep(random.randint(1,5))


process_all_file()