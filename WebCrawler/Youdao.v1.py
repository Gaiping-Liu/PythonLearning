#!/usr/bin/env python
#encoding: utf-8  


'''

'''

import re
import time
#import thread
import urllib
import urllib.request
#import urllib2
#import urllib.request.quote
import random

S_Word = ''
class Spider_Youdao:
    # ???
    def _init_(self):
        #????
        self.run = True

    #???????
    def SearchWord(self, searchWord):
        global S_Word
        S_Word = "hi"

        return S_Word

    #??URL
    def GetUrl(self, searchWord):
        SWord =searchWord #self.SearchWord(searchWord)
        #????????
        #print(urllib.request.quote(SWord))
        if urllib.request.quote(SWord) == SWord:
            MyUrl = "http://dict.youdao.com/w/"+urllib.request.quote(SWord)+"/#keyfrom=dict2.top"
            return MyUrl

    #????
    def GetPage(self, searchWord):
        
        try:#??URL
            Youdao_Url = self.GetUrl(searchWord)
            #????????
            user_agent = 'Mozilla/5.0(X11;Ubuntu;Linux x86_64;rv:32.0)Gecko/20100101 Firefox/32.0'
            headers = {'User-Agent':user_agent}
            req = urllib.request.Request(Youdao_Url,headers = headers)
            Res = urllib.request.urlopen(req)
            #????????????Unicode??
            ResultPage =  Res.read().decode("utf-8")
            return ResultPage
        except Exception as e:
            return ''


    #??????????
    def ExtractPage(self, searchWord):
        #????
        MyPage = self.GetPage(searchWord)
        #???????????
        try:
            myItems = re.search(r'<span class="pronounce">\u7F8E\n.*<span class="phonetic">\[(.+?)\]',MyPage)
            keyWords = re.search(r'<span class="keyword">(.+?)</span>',MyPage)
            #print(myItems.group(0))
            #print(myItems.group(1))
            return keyWords.group(1), myItems.group(1)
        except Exception as e:
            return '', ''
        
    #????
    def Start(self):
        with open(r'E:\temp\youdaodump\all.enUS.lexicon.full.txt','r', encoding='utf-8') as rf:
            allLines= rf.readlines()
        i=3743%1000
        n='4'
        for line in allLines[3745:]:
           if i<1000:
               outputPath = r'E:\temp\youdaodump\all.enUS.lexicon_'+n+r'.youdao.txt'
               with open(outputPath, 'a+', encoding='utf-8') as wf:
                    global S_Word
                    S_Word = line.strip()
                    keyword, result = self.ExtractPage(S_Word)
                    outputline = S_Word+ '\t'+ keyword +'\t' +result+'\n'
                    print(outputline)
                    wf.write(outputline)
                    time.sleep(random.randint(1,10))
               i = i+1
               if i==1000:
                   i=0
                   n=str(int(n)+1)
                   time.sleep(random.randint(10,15))


if __name__ == '__main__':
    mydict = Spider_Youdao()
    mydict.Start()