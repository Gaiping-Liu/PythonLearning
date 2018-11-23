#!/usr/bin/env python
#encoding: utf-8  


import re
import time
import urllib
import urllib.request
import random

class Spider_Familyeducation:
    # init
    def _init_(self):
        self.run = True

    #init URL
    def GetUrl(self, pageID):
        curPageID =pageID #self.SearchWord(searchWord)
        #print(urllib.request.quote(SWord))
        if urllib.request.quote(curPageID) == curPageID:
            MyUrl = "https://www.familyeducation.com/baby-names/browse-origin/surname/chinese?page="+urllib.request.quote(curPageID)
            return MyUrl

    #get page
    def GetPage(self, pageID):
        
        try:
            Cur_Url = self.GetUrl(pageID)
            user_agent = 'Mozilla/5.0(X11;Ubuntu;Linux x86_64;rv:32.0)Gecko/20100101 Firefox/32.0'
            headers = {'User-Agent':user_agent}
            req = urllib.request.Request(Cur_Url,headers = headers)
            Res = urllib.request.urlopen(req)
            ResultPage =  Res.read().decode("utf-8")
            return ResultPage
        except Exception as e:
            return ''

    #Extract content
    def ExtractPage(self, pageID):
        MyPage = self.GetPage(pageID)
        try:
            myItems = re.findall(r'<li>.+?<a href="/baby-names/name-meaning/.+?>(.+?)</a>.+?</li>',MyPage, re.S)
            #keyWords = re.search(r'<span class="keyword">(.+?)</span>',MyPage)
            #print(myItems.group(0))
            #print(myItems.group(1))
            if(myItems != None):
                return myItems
        except Exception as e:
            return '', ''
        
    #????
    def Start(self):
        outputPath = r'E:\Frontend\en-US\Outlook\PersonNameDump\familyeducation.surname.chinese.txt'
        with open(outputPath, 'a+', encoding='utf-8') as wf:
            for i in range(8):
                results = self.ExtractPage(str(i))
                for item in results:
                    #print(item[0])
                    output = item+'\n'
                    wf.write(output)
                time.sleep(random.randint(0,2))


if __name__ == '__main__':
    mydict = Spider_Familyeducation()
    mydict.Start()
