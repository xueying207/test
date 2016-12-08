#coding=utf-8

from appdata import *
import api
from yzm import *
import pyodbc


class sqltest():

    def __init__(self):  #连接数据库

        self.SERVER="172.16.1.102"
        self.username='WP_User'
        self.password='aqswdefrgt'
        self.sqltxt='DRIVER={SQL Server};SERVER='+self.SERVER+';UID='+self.username+';PWD='+self.password
        self.cnxn = pyodbc.connect(self.sqltxt)
        self.cursor = self.cnxn.cursor()

    def sqlrun(self,sql):  #执行SQL
        x=self.cursor.execute(sql)
        #self.autocommit(False)
        return x

    def sqlclose(self):
        self.cnxn.close()



def log(r1):   #保存值到本地
    #x=time.strftime("%Y-%m-%d", time.localtime())
    x1="E:/testlog.txt"
    fo = open(x1,"a")
    #r2=r1.encode('utf-8')
    fo.write(r1);
x = sqltest()

mobile = 13900139001
for i in range(1,999,1):
    try:
        code = {}
        code["SendType"] = "1"
        code["Mobile"] = str(mobile)
        x1 = api.getapi('GetVerificationCode',code,key)
        db = Database()
        x2=db.read('WPVCode:','WP_IOSIphone1.0',mobile)
        login = {}
        login["Mobile"] = str(mobile)
        code1 = "123456" + x2
        print code1
        login["ReferenceNumber"] = api.wpdes(str(code1),deskey)
        x3 = api.getapi('UserMobilephoneLogin',login,key)
        sql = "select UserPwd from [WP_User_V2].[dbo].[UserInfo] where mobile = '"+str(mobile)+"'"
        print sql

        p = x.sqlrun(str(sql))
        p0 = x.cursor.fetchone()
        p1 =  p0[0]
        pwd = api.wpdes(str(p1),deskey)
        getuser = {}
        getuser["UserName"] = str(mobile)
        getuser["Password"] = pwd
        x3 = api.getapi('UserLogin',getuser,key)
        log(x3+"\n")
        mobile = mobile +1
    except:
        log(str(mobile) +"请求出错，请记录"+"\n")