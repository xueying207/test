#coding=utf-8
import requests
import sqldate
import apitest

dir1='E:/apitest/hytest/'
http="https://testbj.channel.wangpiao.com/WebConfidential/WPConfidentialService.asmx/"
key= "test"
deskey="eltcwang"
UserName="wangpiao"
Password="123456"
Des_IV = "\x12\x34\x56\x78\x90\xAB\xCD\xEF" # 自定IV向量
#cityID="1"
#jsq=0

def getuser(x):  #获取用户手机号，密码，用户ID
    username=[]
    userid=[]
    password=[]
    x=sqldate.sqltest()
    y=x.sqlrun("select mobile,userID,UserPwd from 	[WP_User_V2].[dbo].[UserInfo] where mobile <>'' and mobile like '13%'")
    for i in range(x):
        z = y.fetchone()
        username.append(z[0])
        userid.append(z[1])
        password.append(z[2])
        #jprint
    x.sqlclose()
    return username,userid,password


def getapi(APINAME,data,key1):   #请求接口信息
    api = apitest.getpar(APINAME,data,key1)
    url=http+APINAME
    r = requests.post(url,api)
    return r


def GetCinemaListV2(cityID): #获取影院列表
    data={}
    data['CityID']=cityID
    data['AreaName']=""
    data['UserID']=""
    data['CurrentPage']="1"
    #CinemaID   要使用的数据
    return data


