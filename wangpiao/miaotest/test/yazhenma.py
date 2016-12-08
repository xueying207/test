#coding=utf-8
import redis
import demjson
import requests
import hashlib
import base64
from pyDes import *
import urllib

class Database:
    def __init__(self):
        self.host = '172.16.0.21'
        self.port = 6377

    def write(self,WPVCode,wangpiao,number,):
        try:
            key = '_'.join([WPVCode,wangpiao,str(number),"_String"])
            val = "85daa95eb8783e946958f77ff3d5897e|2016-09-20 17:38:23"
            r = redis.StrictRedis(host=self.host,port=self.port)
            r.set(key,val)
        except Exception, exception:
            print exception

    def read(self,WPVCode,wangpiao,number,):
        try:
            key = ''.join([WPVCode,wangpiao,str(number),"_String"])
            r = redis.StrictRedis(host=self.host,port=self.port)
            value = r.get(key)
            #print value
            return value[0:6]
        except Exception, exception:
            print wangpiao+"渠道中手机号还没有获取到验证码"

class req:
    def __init__(self):
        UserName='AndroidV1_wangpiao'
        Password='ZIfEjSli'
        Des_IV= "\x12\x34\x56\x78\x90\xAB\xCD\xEF"

    def md5test(self,str):
        m=hashlib.md5()
        #x=str+key
        m.update(str)
        str1=m.hexdigest()
        return str1

    def wpdes(self,str,key):
        Des_IV= "\x12\x34\x56\x78\x90\xAB\xCD\xEF"
        k =des(key, CBC,Des_IV, padmode=PAD_PKCS5)
        EncryptStr = k.encrypt(str)
        #print "Encrypted: " , EncryptStr

        return base64.b64encode(EncryptStr) #转base64编码返回

    #def jiukou1(self,number,key):



if __name__ == '__main__':
    db = Database()
    rs = req()
    #db.write('WPVCode:','Androidwangpiao',18101360695)
    x1=db.read('WPVCode:','WP_AndroidV1.0',13693031600)
    print x1
    x2=db.read('WPVCode:','WP_IOSIphone1.0',13693031600)
    print x2
    #y=rs.md5test(x)
    #y1=rs.wpdes(str(y),"eltcwang")
    #print y1.encode('utf-8')

#"saPkcUlDPZsm0h/bvXTYPrPrxBQ94Y5nCbmzlxFGVV%2bptPIxfgkFTQ\u003d\u003d"}]}]}
#"YiHLArT0VLwA0UeoakbtWzv55LG8FuhIzba8Zl%2bsvnl0h7aOpAzaLQ\u003d\u003d"}]}]}
#TTR1ZlNEV2p0Znl1NnRrM09EK3V5OHF4b2cwaXl3RktQM05IVHhrY0lLQXI2ajMxaE9HV1RBPT0
#x='M4ufSDWjtfyu6tk3OD+uy8qxog0iywFKP3NHTxkcIKAr6j31hOGWTA=='
#print  urllib.quote(x)   #U对字符进行URL编码
