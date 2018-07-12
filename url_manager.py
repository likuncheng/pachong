# -*- coding:utf-8 -*-
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls)!=0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        num=0
        for url in urls:
            num+=1
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.add(url)
                #print '执行批量增加',num,url
    def display(self):
        print '-'*60
        print 'new_urls目前的数目：',len(self.new_urls)
#         for i in self.new_urls:
#             print i
        print 'old_urls目前的数目：',len(self.old_urls)
        print '-'*60
    
    
    
    
    



