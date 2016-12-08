#coding=utf-8
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
        return x

    def sqlclose(self):
        self.cnxn.close()

