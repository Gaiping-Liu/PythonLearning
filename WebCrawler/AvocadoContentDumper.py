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

def extract_contents(inputFilePath, logs ,nameAddressAndFreq, fromAddress, allAddress):
    tempLine, fromName, to, cc, bcc = '','','','',''
    fo = open(inputFilePath, 'r')
    for line in fo.readlines():
        line = line.strip()
        colonIndex = 0
        if(line.find(':')>(-1)):
            colonIndex = line.find(':')
        element = line[0:colonIndex]
        content = line[colonIndex:].lstrip(':').strip()
        shouldStop = False

        if element == 'From':
            fromName = content # tempLine now is from address;
            continue;
        elif element == 'To':
            to = content
            continue;
        elif element == "Cc":
            cc = content; # tempLine now is cc address;
            continue;
        elif element == "Bcc":
            bcc = content; # tempLine now is bcc address;
            continue;
        elif element == "Subject":
            #shouldStop = True;
            break;

    fo.close()
    
    if(name_lock.acquire(True)):
        if (fromName != ""):
            if (fromName in nameAddressAndFreq):
                     nameAddressAndFreq[fromName] +=1 
            else:
                 nameAddressAndFreq[fromName] = 1
            if (fromName not in fromAddress):
                fromAddress.append()
        if (to != ""):
            if (to in nameAddressAndFreq):
                 nameAddressAndFreq[to] +=1 
            else:
                 nameAddressAndFreq[to] = 1
        if (cc != ""):
            if (cc in nameAddressAndFreq):
                 nameAddressAndFreq[cc] +=1 
            else:
                 nameAddressAndFreq[cc] = 1
        if (bcc != ""):
            if (bcc in nameAddressAndFreq):
                 nameAddressAndFreq[bcc] +=1 
            else:
                 nameAddressAndFreq[bcc] = 1
        name_lock.release()

    if (fromName == "" and to == ""):
         logs.append(inputFilePath)


def process_all_file():
    #inputDir = r'E:\Frontend\en-US\Outlook\PersonName\A\data\text'
    inputDir = r'E:\Frontend\en-US\Outlook\PersonName\A\testData'
    outputDir = r'E:\Frontend\en-US\Outlook\PersonName\A\output'
    outputDisplayName = os.path.join(outputDir, r'displayname.all.txt')
    outputLog = os.path.join(outputDir, r'log.all.txt')
    outputFromAddress = os.path.join(outputDir, r'log.fromaddress.txt')
    outputAllAddress = os.path.join(outputDir, r'log.alladdress.txt')


    i=1
    logs= []
    fromAddresses = []
    allAddresses = []
    nameAddressAndFreq = {}
    #inputFiles = os.listdir(inputDir)
    #for i in range(0, len(inputFiles)):
    for root, subdirs, files in os.walk(inputDir):
        for fn in files:
            if fn.endswith("EM.txt"):
                path = os.path.join(root, fn)
                print(i)
                i = i+1
                if os.path.isfile(path):
                    Thread(target = extract_contents, args = (path, logs ,nameAddressAndFreq, fromAddresses, allAddresses)).start()
                    #extract_contents(path, logs ,nameAddressAndFreq)
    with open(outputDisplayName, 'a+', encoding='utf-8') as wf:
        for item in nameAddressAndFreq:
            output = item + '\t' + str(nameAddressAndFreq[item]) + '\n'
            wf.write(output)

    with open(outputLog, 'a+', encoding='utf-8') as wf:
        for item in logs:
            wf.write(item+'\n')
    with open(outputFromAddress, 'a+', encoding='utf-8') as wf:
        for item in fromAddresses:
            wf.write(item+'\n')
    with open(outputAllAddress, 'a+', encoding='utf-8') as wf:
        for item in allAddresses:
            wf.write(item+'\n')

process_all_file()
