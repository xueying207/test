#-coding:UTF8-*-
from api import *
from excel import *
from sjjc  import *


def test():
    xls=getfile(dir1)
    #print xls[1]
    for i in xls:

        i= i.decode("gbk")

        print i,"准备执行"
        #try:
        api,url,ruq = apidata(dir1+i,deskey)

        url1=http+url  #生成完成接口地址
        print "请求地址为："+str(url1)
        num=0

        for j in (api ):
            #print api
            num = num + 1
            y= mtest.getpar(url, j, key)  #生成Parameters
            #print y
            #tem=time.time()
            x=requtest(y,url1,ruq)
            #tem1=time.time()
            #print tem1-tem
            z= i.split(".")[0]
            runtest(num,x,z,y)
            #jc(x,y,i,url)
        print i,"接口用例执行完成，准备执行下一个用例"
        #except:
            # i,"文件内容出错，请检查"
    print "目录下所有用例执行完成，执行结果信息请查看日志文件"

for i in range(2):
    num = 'thread'+str(i)
    num = test()

for j in range(1):
    ai=str(j)
    num = 'thread'+ai
    num.start()