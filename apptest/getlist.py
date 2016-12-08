#coding:utf-8
import requests
import os
import city
def Getlist():  #获取热映影片
    data1={}
    data1['osVersion'] ="4.2.2"
    data1['imei'] ="864895027568649"
    data1['appkey'] ="android2009"
    data1['format'] ="xml"
    data1['osType'] ="ANDROID"
    data1['appSource'] ="AS06"
    data1['mobileType'] ="HTC D820u"
    data1['version'] ="1.0"
    data1['sign'] ="A9F61CC07B1CCC563E654BFD6445051B"
    data1['pointx'] ="116.616876"
    data1['timestamp'] ="2016-04-15 15:57:37"
    data1['citycode'] ="110000"
    data1['pointy'] ="39.914008"
    data1['v'] ="1.0"
    data1['appVersion'] ="6.6.0"
    data1['mnet'] ="WIFI"
    data1['method'] ="com.gewara.mobile.movie.getCurHotMovies"
    data1['signmethod'] ="MD5"
    data1['mprovider'] ="310260"
    data1['apptype'] ="cinema"
    data1['deviceId'] ="507B9D29A100"
    #data1=demjson.encode(data1)
    r1 = requests.post("http://103.20.250.42/router/rest ", data=data1)
    print r1.text

    city.log(r1.text)
Getlist()