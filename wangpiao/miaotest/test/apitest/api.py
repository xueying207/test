#coding=utf-8
import os
import time

import requests
import xlrd

import mtest


#from run import *


def apidata(xls,key):

    data = xlrd.open_workbook(xls)
    table = data.sheets()[0]
    nrows = table.nrows #获取行数
    #print nrows
    ncols = table.ncols #获取列数
    url= table.cell(1,3).value  #获取URL
    req= table.cell(3,3).value  #获取接口方式
    data=[]
    data1={}
    for i in range(nrows ): #循环获取行值
        try:
            apiname=table.cell(i+1,0).value   #获取参数名
            #print nrows,i,apiname
            apiname1=apiname.encode("utf-8")
            if apiname1 == "end" or apiname1 == "" :

                #print "读取到end，进行参数调整"
                data.append(data1)
                data1={}
                #print data1,data
                continue
            apidata=table.cell(i+1,1).value  #获取参数的值
            des=table.cell(i+1,2).value
            #print des
            apidata1=apidata.encode("utf-8")
            if des=="":
                data1[apiname1]=apidata1
            else:
                desx= mtest.wpdes(apidata1, key)

                data1[apiname1]=desx

        except Exception:
            pass
    print "EXCEL文件获取接口参数成功"
    return data,url,req  #返回参数以及URL

def log(r1,t1,dir):   #保存值到本地
    x=time.strftime("%Y-%m-%d", time.localtime())
    x1=dir+t1+x+".txt"
    fo = open(x1,"a")
    #r2=r1.encode('utf-8')
    fo.write(r1);

def requtest(api,url,ruq):
    if  ruq =='post':
        tem=time.time()
        r = requests.post(url,api,verify=False)
        tem1=time.time()
        print tem1 - tem
        #print r.status_code
    elif ruq == "get":
        r = requests.get(url,api,verify="E:/\apitest/\test.cer")

    else:
        print "没有设置协议类型，请设置"
    #print r.text
    #print "接口请求成功"
    #print r.status_code
    return r


def getfile(name):   #获取目录下的所有excel文件名
    test=os.listdir(name)   #设置文件目录
    test.sort()     #对目录下文件进行排序
    filename=[]   #定义存excel文件的列表名
    #file=[]
    #print  "222"
    for i in test:   #对目录下的文件进行循环
        x= i.split(".").pop()   #获取文件的扩展名
        #y= i.split(".")[0]
        if x =="xlsx" or x =="xls":   #判断扩展名
            #print i
            filename.append(i)    #把当前文件添加到列表中
            #file.append(y)
    return filename



#print api







