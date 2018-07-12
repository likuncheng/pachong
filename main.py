# -*- coding:utf-8 -*-
from imooc import url_manager, html_downloader, html_parser, html_outputer
class Spider_Main():
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.DownLoad()
        self.parser = html_parser.Parser()
        self.outputer = html_outputer.OutPuter()
        self.count=1
    def craw(self,root_url):
        
        self.urls.add_new_url(root_url)
        
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print '解析页面  ',new_url
                #print 'craw %d : %s' % (str(self.count),new_url)
                html_content = self.downloader.download(new_url)
                
                new_urls,new_data = self.parser.Parsers(new_url,html_content)
#                 if new_urls == None or new_data == None:    
#                     continue
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_new_data(new_data)   
                self.urls.display()
                #break
                self.count+=1
                if self.count==100:
                    break
            except:
                print 'craw failed'  
        
               
if __name__ =='__main__':
    root_url = 'http://www.27270.com/'
    obj_spider_main = Spider_Main()
    obj_spider_main.craw(root_url)
        