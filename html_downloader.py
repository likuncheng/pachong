# -*- coding:utf-8 -*-
import requests
class DownLoad(object):

    def download(self,new_url):
        
        if new_url is None:
            return None
        if new_url[:7]!='http://':
            print '不是http://类型的：',new_url
            return None
        try:
            response=requests.get(new_url, stream=True)
        except:
            print '遇到无法解析的url了'
        if response.status_code!=200:
            return  None
        print type(response.text.encode('utf-8'))
        return response.text.encode('utf-8')
        
        
        