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
    tempAddre, fromAddre, toAddre, ccAddre, bccAddre = '','','','',''
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
            tempLine = content # tempLine now is from address;
            continue;
        elif element == 'To':
            fromName = tempLine; # should get from address ready
            fromAddre = tempLine;
            tempLine = content
            continue;
        elif element == "Subject":
            to = tempLine; # should get to address ready
            toAddre = tempLine;
            tempLine = "";
            continue;
        elif element == "Cc":
            tempLine = content; # tempLine now is cc address;
            
            continue;
        elif element == "Mime-Version":
            cc = tempLine; # should get cc address ready
            ccAddre = content;
            tempLine = "";
            continue;
        elif element == "Bcc":
            tempLine = content; # tempLine now is bcc address;
            continue;
        elif element == "X-From":
            bcc = tempLine; # should get bcc address ready
            bccAddre = tempLine;
            tempLine = content; # tempLine now is from name;
            continue;
        elif element == "X-To":
            fromName = (tempLine + "\t" + fromName).strip(); # should get from name ready
            tempLine = content; # tempLine now is to name;
            continue;
        elif element == "X-cc":
            to = (tempLine + "\t" + to).strip(); # should get to name ready
            tempLine = content; # tempLine now is cc name;
            continue;
        elif element == "X-bcc":
            cc = (tempLine + "\t" + cc).strip(); # should get cc name ready
            tempLine = content; # tempLine now is bcc name;
            continue;
        elif element == "X-Folder":
            bcc = (tempLine + "\t" + bcc).strip(); # should get bcc name ready
            shouldStop = True;
            break;
        elif element == "":
            tempLine = tempLine + " " + content; # this maybe not break From or To or CC or Bcc
            continue;
        else:
            # other element that not contains any useful info
            continue;

        if (shouldStop):
            break;
    fo.close()
    
    if(name_lock.acquire(True)):
        if (fromName != ""):
            if (fromName in nameAddressAndFreq):
                     nameAddressAndFreq[fromName] +=1 
            else:
                 nameAddressAndFreq[fromName] = 1
            if( fromAddre not in fromAddress):
                fromAddress.append(fromAddre)
            if( fromAddre not in allAddress):
                allAddress.append(fromAddre)
        if (to != ""):
            if (to in nameAddressAndFreq):
                 nameAddressAndFreq[to] +=1 
            else:
                 nameAddressAndFreq[to] = 1
            for add in toAddre.split(','):
                if (add.strip() not in allAddress):
                    allAddress.append(add.strip())
        if (cc != ""):
            if (cc in nameAddressAndFreq):
                 nameAddressAndFreq[cc] +=1 
            else:
                 nameAddressAndFreq[cc] = 1
            for add in ccAddre.split(','):
                if (add.strip() not in allAddress):
                    allAddress.append(add.strip())
        if (bcc != ""):
            if (bcc in nameAddressAndFreq):
                 nameAddressAndFreq[bcc] +=1 
            else:
                 nameAddressAndFreq[bcc] = 1
            for add in bccAddre.split(','):
                if (add.strip() not in allAddress):
                    allAddress.append(add.strip())
        name_lock.release()

    if (fromName == "" and to == ""):
         logs.append(inputFilePath)


def process_all_file():
    inputDir = r'E:\Frontend\en-US\Outlook\PersonName\E\RawData\enron_mail_20150507\maildir'
    #inputDir = r'E:\Frontend\en-US\Outlook\PersonName\E\testData'
    outputDir = r'E:\Frontend\en-US\Outlook\PersonName\E\output'
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
            path = os.path.join(root, fn)
            print(i)
            i = i+1
            if os.path.isfile(path):
                Thread(target = extract_contents, args = (path, logs ,nameAddressAndFreq, fromAddresses, allAddresses)).start()
                #extract_contents(path, logs ,nameAddressAndFreq, fromAddresses, allAddresses)
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
