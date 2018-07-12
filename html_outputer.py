# -*- coding:utf-8 -*-
import requests
class OutPuter(object):
    
    def __init__(self):
        self.countt = 1
       
    def collect_new_data(self,new_data):
        
        if new_data is None or len(new_data)==0:
            return
        
        for i in new_data:
            #print i
            course = 'D:\python\Test\img\%s' % (str(self.countt)+'_img.jpg')
            response=requests.get(i, stream=True)
            with open(course, 'wb') as fd:
                for chunk in response.iter_content(128):
                    fd.write(chunk)
                print '下载完成'+str(self.countt)+'_img.jpg'
            self.countt+=1
        print "OutPuter ",len(new_data)
            
            
        
        
        
    
    



