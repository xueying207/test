#coding:utf-8
import requests
import os


data1={}
data1['Parameters']='{"InputData":[{"APIName":"GetFilmHotAndReflected","Parameters":[{"CityID":"1","Type":"1"}]}]}'
data1['UserName'] ="Androidwangpiao"
data1['Sign']="c61bbf3eb72814ade804b557b8db25e3"
data1['Password']="7cPOdDWnewc="
#data1=demjson.encode(data1)
r = requests.post("http://wifi.api.wangpiao.com/Mobile_V4/WebServiceV2.asmx/GetFilmHotAndReflected", data=data1)
print r.text
