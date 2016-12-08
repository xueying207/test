#coding:utf-8
import requests
import os

def GetFilm():  #获取热映影片
    data1={}
    data1['Parameters']='{"InputData":[{"APIName":"GetFilmHotAndReflected","Parameters":[{"CityID":"51","Type":"1"}]}]}'
    data1['UserName'] ="Androidwangpiao"
    data1['Sign']="a6bcc05cb02a82facde859596451cf30"
    data1['Password']="7cPOdDWnewc="
    #data1=demjson.encode(data1)
    r1 = requests.post("http://wifi.api.wangpiao.com/Mobile_V4/WebServiceV2.asmx/GetFilmHotAndReflected", data=data1)
    print r1.text