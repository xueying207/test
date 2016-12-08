#coding:utf-8
import requests
import os
import logging
import time

#获取城市ID
def getcity():
    data1={}
    data1['Parameters']='{"InputData":[{"APIName":"GetCityList","Parameters":[{"cityID":""}]}]}'
    data1['UserName'] ="Androidwangpiao"
    data1['Sign']="ba81642b5a16a63260a74d5e6e83e8a0"
    data1['Password']="7cPOdDWnewc="
    #data1=demjson.encode(data1)
    r = requests.post("http://wifi.api.wangpiao.com/Mobile_V4/WebServiceV2.asmx/GetCityList", data=data1)
    print r.text
    return r

def Getlist():  #获取热映影片
    data1={}
    data1['Parameters']='{"InputData":[{"APIName":"GetCinemaListV2","Parameters":[{"AreaName":"","CinemaName":"","CityID":"51","CurrentPage":"1","LonLat":"116.616876|39.914008","UserID":""}]}]}'
    data1['UserName'] ="Androidwangpiao"
    data1['Sign']="6516b67fc142862feaaa2cf23a2428fa"
    data1['Password']="7cPOdDWnewc="
    #data1=demjson.encode(data1)
    r = requests.post("http://wifi.api.wangpiao.com/Mobile_V4/WebServiceV2.asmx/GetCinemaListV2", data=data1)
    r1=r.text
    print r.text

def GetFilm():  #获取热映影片
    data1={}
    data1['Parameters']='{"InputData":[{"APIName":"GetFilmHotAndReflected","Parameters":[{"CityID":"51","Type":"1"}]}]}'
    data1['UserName'] ="Androidwangpiao"
    data1['Sign']="a6bcc05cb02a82facde859596451cf30"
    data1['Password']="7cPOdDWnewc="
    #data1=demjson.encode(data1)
    r1 = requests.post("http://wifi.api.wangpiao.com/Mobile_V4/WebServiceV2.asmx/GetFilmHotAndReflected", data=data1)
    print r1.text
def log(r1):
    x=time.strftime("%Y-%m-%d %H;%M;%S", time.localtime())
    x1="log\\getcity"+x+".html"
    fo = open(x1,"w")
    r2=r1.encode('utf-8')
    fo.write(r2);
x=getcity()
x1=x.json()
print x1["OutputData"]
