# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
class Parser(object):
       
    def _acquire_new_urls(self, new_url, soup):
        try:
            new_urls = set()
            if len(new_urls)!=0:
                new_urls.clear()
            links = soup.find_all('a')
            for link in links:
                new_url = link['href']
                new_urls.add(new_url)
                #print new_url        
            print 'parser new_urls',len(new_urls)
            
            return new_urls
        except:
            print '_acquire_new_urls failed'
            return None
    
    def _acquire_new_data(self, new_url, soup):
        new_data = set()
        if len(new_data)!=0:
            new_data.clear()
        links = soup.find_all('img')
        for link in links:
            new_url = link['src']
            new_data.add(new_url)
            #print new_url        
        print 'parser new_data',len(new_data)
        return new_data

    def Parsers(self,new_url,html_content):
        if new_url is None or html_content is None:
            print 'NoneNoneNone'
            return None,None
        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        new_urls = self._acquire_new_urls(new_url,soup)
        new_data = self._acquire_new_data(new_url,soup)
        print "="*60
        return new_urls,new_data