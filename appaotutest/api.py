#coding=utf-8
import demjson
import hashlib
import base64
from pyDes import *
from appdata import *
import urllib
import requests

def getpar(APIName,data,key):
    #m=hashlib.md5()
    data1={}
    data2={}
    data3={}
    data1["APIName"]=str(APIName)
    data1["Parameters"] = [data]
    data3["InputData"]=[data1]
    #{'UserName': 'Androidwangpiao', 'Password': '7cPOdDWnewc=', 'Parameters': '{"InputData":[{"APIName":"GetFilmHotAndReflected","Parameters":[{"C":"1","Type":"1"}]}]}', 'S': 'c61bbf3eb72814ade804b557b8db25e3'}
    data3=demjson.encode(data3)
    #key='Wp16dY@z^F283QVj'
    m=hashlib.md5()
    x=data3+key#+Password
    #print x
    m.update(x)
    json1 = m.hexdigest()
    #print json1
    data2['UserName']= UserName
    data2[ 'Password']=Password
    data2[ 'Parameters']=str(data3)
    data2['Sign']= json1
    #data4={'UserName': 'Androidwangpiao', 'Password': '7cPOdDWnewc=', 'Parameters':data1,'Sign': 'c61bbf3eb72814ade804b557b8db25e3'}
    #data5=demjson.encode(data4)
    return data2

#Des_IV =  # 自定IV向量


def wpdes(str,Des_Key):

    #print "222"
    k =des(Des_Key, CBC,Des_IV, padmode=PAD_PKCS5)

    EncryptStr = k.encrypt(str)
    #print "Encrypted: " , EncryptStr
    desx1=base64.b64encode(EncryptStr)
    desx=urllib.quote_plus(desx1)
    return desx #转base64编码返回

def jmdes(str,Des_Key):

    #print "222"
    k =des(Des_Key, CBC,Des_IV, padmode=PAD_PKCS5)

    EncryptStr = k.decrypt(str)
    #print "Encrypted: " , EncryptStr
    #desx1=base64.b64encode(EncryptStr)
    #desx=urllib.quote(desx1)
    return EncryptStr #转base64编码返回


def getapi(APINAME,data,key1):   #请求接口信息
    #print data
    api = getpar(APINAME,data,key1)
    url=http+APINAME
    print url
    print api
    r1 = requests.post(url,api,verify=False)
    print r1.text
    #r= r1.text
    #print r
    return r1.text

