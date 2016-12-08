#coding=utf-8

def cfpd(self,str1,num):
    str2=""
    #while (1==1):
    if str2==str1:
        str1=str1+1
        if str1==num:
            self._current_application().back()
            str1=1
            #break
    else:
        str1=1
