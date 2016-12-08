#-coding:UTF8-*-
import xlrd

import mtest


def apidata(xls,key):
    print xls
    excel = xlrd.open_workbook(xls)
    #data =  exdata(xls)
    table = excel.sheets()[0]
    table1 = excel.sheets()[1]
    nrows1 = table1.nrows
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
            if des=="": #对参数进行加密
                data1[apiname1]=apidata1
            else:
                desx= mtest.wpdes(apidata1, key)
                data1[apiname1]=desx
            #print "222"
        except Exception:
            pass


    print "EXCEL文件获取接口参数成功"



    return data,url,req  #返回参数以及URL


def jkjc(xls):
    try:
        data1 = xlrd.open_workbook(xls)
        #data =  exdata(xls)
        table = data1.sheets()[1]
        nrows = table.nrows #获取行数
        data=[]
        print data
        #del data[:]
        #data=[]
        for i in range(nrows ):
            apiname=table.cell(i+1,0).value   #获取参数名
            print apiname
            apiname1=apiname.encode("utf-8")
            if apiname1 == "end" or apiname1 == "" :
                    #print "读取到end，进行参数调整"
                    print data1,data
                    continue
            else:
                #print apiname1
                data.append(apiname1)
                print data
        #print data
    except:
        pass
    print data
    return #data



