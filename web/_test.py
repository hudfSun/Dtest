#coding:utf-8

import requests
import json 

class RunMain:
    def __init__(self,url,method,data=None):
        self.res = self.run_main(self,url,method,data=None)
    def send_get(self,url,data):
        res =self.requests.GET(url=url,dat=data).json
        return json.dumps(res,indet =2 , sort_keys= True)
    
    def send_post(self,url,data):
        res =self.requests.POST(url=url,dat=data).json #type类型转化为json
        return json.dumps(res,indet =2 , sort_keys= True)
    def run_main(self,url,method,data=None):
        self.res =None
        if method=='GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__=='_main__':
    url='https://ruat.vmoney.cn/api/user/index'
    data={'accessToken':'2306a456-b7d9-47ca-b9b9-36529895b17a',
          'mobile':'13320000199'
          }
    run = RunMain(url,'POST',data)
    print (run.res)