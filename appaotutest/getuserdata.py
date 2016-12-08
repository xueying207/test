#coding=utf-8
#获取初始化用户信息以及影院信息
from sqldata import *


#x=1
#jsq = 1

def getuser(x):  #获取用户手机号，密码，用户ID
    username=[]
    userid=[]
    password=[]
    x=sqltest()
    y=x.sqlrun("select mobile,userID,UserPwd from 	[WP_User_V2].[dbo].[UserInfo] where mobile <>'' and mobile like '13%'")

    for i in range(0,10,1):
        z = y.fetchone()
        username.append(z[0])
        userid.append(z[1])
        password.append(z[2])
        #print(username)
    x.sqlclose()
    return username,userid,password

#username,userid,password =getuser(x)



