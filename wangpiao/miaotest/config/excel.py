#-coding:UTF8-*-
import xlrd,demjson
import hashlib
m=hashlib.md5()
data = xlrd.open_workbook('E:\Book1.xlsx')
table = data.sheets()[0]
nrows = table.nrows #获取行数
print nrows
ncols = table.ncols #获取列数
print ncols
for i in range(nrows ):
    #print "第",i,"行"
    x=table.row_values(i)
    #print x, len(x)
    APIName1=table.cell(i+1,0).value
    APIName=APIName1.encode("utf-8")  #定义apiname
    data={}

    try:
        for j in range(ncols-1 ):
            x1=2*j+1
            test=table.cell(i+1,x1).value
            test1=test.encode("utf-8")  #定义参数名
            if test1=="":
                continue
            #print test1
            x2=table.cell(i+1,x1+1).value
            print x2
            test2=x2.encode("utf-8")
            data[test1]=test2   #给参数名赋值
            #print data,j
    except Exception, e:
        print e
    data1=[{"APIName":APIName,"Parameters":[data]}]
    data2={"InputData":data1}
    #print data2
    data3=demjson.encode(data2)
    key='Wp16dY@z^F283QVj'
    json=m.update(data3+key)
    json1 = m.hexdigest()
    print "AIPNAM是：",APIName
    print "Parameters的数据是：",data3
    print "json的值是：",json1
 #{“InputData”: [{“APIName”: “UserLogin”,” Parameters”:[  {“UserName”:”wangpiao”,”Password”:”3w9(a$as12”}]}]}