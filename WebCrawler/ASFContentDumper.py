#!/usr/bin/env python
#encoding: utf-8  


import requests
import bs4
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import os
from threading import Thread
import threading


name_lock = threading.Lock()
subject_lock = threading.Lock()
body_lock = threading.Lock()

def extract_contents(inputFilePath, outputDisplayName ,outputSubjectName, outputBodyName):
    soup = BeautifulSoup(open(inputFilePath))
    sender, subject, body =None, None, None
    try: 
        froms = soup.find(name ='tr', attrs ={ 'class':'from'})
        sender = froms.find(name ='td', attrs ={'class':'right'}).string
        if sender.count('"') !=0 :
            sender = sender[0:sender.rfind('"')].replace('"','')
            if sender =='':
                sender = None
        else:
            sender = None
    except Exception as e:
        sender = None

    try: 
        subjectTag = soup.find(name ='tr', attrs ={ 'class':'subject'})
        subject = subjectTag.find(name ='td', attrs ={'class':'right'}).get_text()

    except Exception as e:
        subject = None

    try:
        body = soup.find(name ='pre').get_text()
    except Exception as e:
        body = None

    if sender != None:
        if(name_lock.acquire(True)):
            with open(outputDisplayName, 'a+', encoding='utf-8') as wf:
                output = sender + '\n'
                wf.write(output)
            name_lock.release()
    if subject != None:
        if(subject_lock.acquire(True)):
            with open(outputSubjectName, 'a+', encoding='utf-8') as wf:
                output = subject + '\n'
                wf.write(output)
            subject_lock.release()
    if body != None:
        if(body_lock.acquire(True)):
            with open(outputBodyName, 'a+', encoding='utf-8') as wf:
                output = body + '\n'
                wf.write(output)
            body_lock.release()

def process_all_file():
    inputDir = r'\\stcvm-971\Share\Gaiping\ASFMailArchive\mail-archives.apache.org\mod_mbox'
    #inputDir = r'E:\Frontend\en-US\Outlook\ApacheEmail\testdata'
    outputDir = r'E:\Frontend\en-US\Outlook\ApacheEmail\RawData'
    outputDisplayName = os.path.join(outputDir, r'displayname.txt')
    outputSubjectName = os.path.join(outputDir, r'subject.txt')
    outputBodyName = os.path.join(outputDir, r'body.txt')

    i=1
    #inputFiles = os.listdir(inputDir)
    #for i in range(0, len(inputFiles)):
    for root, subdirs, files in os.walk(inputDir):
        for fn in files:
            path = os.path.join(root, fn)
            print(i)
            i = i+1
            if os.path.isfile(path):
                Thread(target = extract_contents, args = (path, outputDisplayName ,outputSubjectName, outputBodyName)).start()
    

process_all_file()