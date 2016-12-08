#coding=utf-8
from api import log
from excel import jkjc
from data import *

def runtest(num,x,txt,y):   #执行并打印日志   num为计数器    X为接口返回数据，text为日志名，y为接口传参
    #from run import dir1
    #print dir1
    y1=""
    y1="第"+str(num)+"次请求数据:"+str(y)+"\n"
    log(y1,txt,dir1)
    #log(y1)
    #x1=eval(x.text)
    y2=""
    y3= x.text
    y2 = "第"+str(num)+"次返回参数："+y3.encode('utf-8')+"\n"
    #y2 = "第"+str(num)+"返回参数："+ str(x.json())+"\n"
    log(y2,txt,dir1)
    if x.ok:
        #z= "第"+num+"次接口请求成功"
        print "第",num,"次接口请求成功"
        #log(z,"test",dir)
        x1=x.json()
        #print x1['OutputData']
        x2= x1['OutputData'][0]['Success']
        #print x1['OutputData'][0]['Data']
        #x3= x2[0]['Data'][0]['Success']
        x3=x1['OutputData'][0]['ErrorInfo']
        if x2 =="true" :
            #z="第"+num+"次接口返回参数正确"
            print "第",num,"次接口返回参数正确"
            #log(z,"test",dir)
        else:

            if x3=='':
                x4=x1['OutputData'][0]["Data"][0]["Message"]
                #print x4
                #z="第"+num+"次接口返回参数报错，错误信息为："+x4
                print "第",num,"次接口返回参数报错，错误信息为：",x4
                #log(z,"test",dir)
            else:
                print "第",num,"次接口返回参数报错，错误信息为：",x3
    else:
        print "第",num,"次接口请求失败"


def jc(x,y,xls,url):
    #try:
    #print "1",x.json(),y
    #from run import xls,dir1
    #print 1
    x1=x.json()   #出参
    #print x1
    #y1=y   #传参

    x2=x1['OutputData'][0]["APIName"]
    #from run import url
    y2=url
    if y2==x2:
        print "接口返回参数名正确"
    else:
        print "接口名返回错误，传参为：",y2,"出参为：",x2
    #print xls,key

    for j in xls:
        j= j.decode("gbk")
        #print dir1+j
        #data=[]
        data=jkjc(dir1+j)
        print data
        for i in (data):
            print i
            try:
                data1= x1['OutputData'][0]["Data"][0][i]
                print"当前接口",i,"参数返回值为：",data1
            except:
                print "当前接口参数",i,"返回出错，请检查日志"
    #except:
        #print "用例没有设置返回参数名，请设置"