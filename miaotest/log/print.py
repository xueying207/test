import os
import time
def log(r1):
    x=time.strftime("%Y-%m-%d %H;%M;%S", time.localtime())
    x1="log\\getcity"+x+".xml"
    fo = open(x1,"w")
    r2=r1.encode('utf-8')
    fo.write(r2);