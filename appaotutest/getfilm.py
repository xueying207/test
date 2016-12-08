#coding=utf-8
from appdata import *
import api
from getuserdata import *

def GetCinemaListV2(cityID): #获取影院列表
    data={}
    data['CityID']=cityID
    data['AreaName']=""
    data['UserID']=""
    data['CurrentPage']="1"
    data['CinemaName']=""
    data['LonLat']=""
    #CinemaID   要使用的数据
    return data

def GetFilmHotAndReflected(cityID):
    data={}
    data['CityID']=cityID
    data['Type']="1"
    return data
username,userid,password =getuser(10)

def getsea(x):
    Film=GetFilmHotAndReflected(cityID)  #获取影院ID
    #print Film
    x1=api.getapi('GetFilmHotAndReflected',Film,key)
    #print x1
    #x1= x1.json()
    CinemaID=[]
    FilmID=[]
    ScreeningPlanNo=[]

    for i in range(x):
        #try:
        y=  x1['OutputData'][0]["Data"][i]["FilmID"]
        #print y
        FilmID.append(y)
        #except:
            #print "1231"
            #break
        Cinema={}
        Cinema["FilmID"] = str(FilmID[i])
        Cinema["CityID"] = cityID
        Cinema["ShowDate"] = "2016-11-25"
        Cinema['AreaName']=""
        Cinema['UserID']=""
        Cinema['LonLat']="116.418122|39.921469"
        Cinema['CurrentPage']="1"
        #film = film.GetFilmInfoToCinema()  #获取影片ID
        #print Cinema
        x2 = api.getapi('GetFilmToCinemaList',Cinema,key)
        #print x2
        #print x2['OutputData'][0]["Data"][0]["CinemaID"]
        CinemaID.append( x2['OutputData'][0]["Data"][0]["CinemaID"])
        ScreeningPlan={}
        ScreeningPlan["CinemaID"]= str(CinemaID[i])  #获取影片场次ID
        ScreeningPlan['CityID']=cityID
        ScreeningPlan['FimlID']=str(FilmID[i])
        x3 = api.getapi('getGetScreeningPlanToCinema',ScreeningPlan,key)
        #x3 = x3.json()
        ScreeningPlanNo = x3['OutputData'][0]["Data"][0]["ScreeningPlanNo"]
        seatlist={}
        seatlist["CinemaID"]=CinemaID[i]
        seatlist['ScreeningPlanNo'] = ScreeningPlanNo[i]
        #seatlist = film.GetSeatList(ScreeningPlanNo)

        x4 = api.getapi('GetSeatList',seatlist,key)
        x4 = x4.json()
        GetEcode={}
        GetEcode["UserID"] = userid[i]
        GetEcode["ShowIndex"] = ScreeningPlanNo[i]
        GetEcode["UserName"] = userid[i]
        GetEcode["Password"] = "ZIfEjSlihUhaXpAYafn7agJNNquwdyFHqocThLiFIuGHTKAyYbqZag%3D%3D"
        GetEcode1 = api.getapi('GetEcodeForShow',GetEcode,key)
        Ecode1=[]
        js=1
        for e in (GetEcode1['OutputData'][0]["Data"]):
            Ecode1=api.jmdes(e["CodeNumber"],deskey)
            js = js+1
            if js <5:
                Ecode = Ecode+str(Ecode1)+"|"
            else:
                Ecode = Ecode+str(Ecode1)
                continue
        seano = 0
        SeatID = ""
        SeatName = ""
        for j in range(x4):
            if x4['OutputData'][0]["Data"][j]["SeatState"]:
                SeatID = SeatID+str(x3['OutputData'][0]["Data"][j]["SeatID"])+"|"
                SeatName = SeatName+str(x3['OutputData'][0]["Data"][j]["SeatName"])+"|"
                seano =seano+1
            elif seano == 4:
                SeatID = SeatID+str(x3['OutputData'][0]["Data"][j+1]["SeatID"])
                SeatName = SeatName+str(x3['OutputData'][0]["Data"][j+1]["SeatName"])
                break
            else:
                continue
            #def CreateSubscript(self,Mobile,SeatID,SeatName,SeatState,jsq):  #创建影票订单
        Subscript={}
        Subscript["CinemaID"] = CinemaID[i]
        Subscript["Mobile"]  = username[i]
        Subscript["PayType"] = "5"
        Subscript["ScreeningPlanNo"]  =ScreeningPlanNo[i]
        Subscript["DeviceNumber"] = "f3d438a9ff853ec4f7331d2a8739af85"
        Subscript["SeatInfo"] = SeatID
        Subscript["SeatName"] = SeatName
        Subscript["UserID"] = userid[i]
        Subscript["Versions"] = "And4.3.5"
        x4 = api.getapi('CreateSubscript',Subscript,key)
        print x4
        SubInfo={}
        SubInfo["UserID"] = userid[i]
        SubInfo["OrderID"] = x4['OutputData'][0]["Data"][0]["OrderID"]
        SubInfo["PayType"] = "1"
        SubInfo["Mobile"] = username[i]
        SubInfo["UserName"] = username[i]
        SubInfo["Password"] ="ZIfEjSlihUhaXpAYafn7agJNNquwdyFHqocThLiFIuGHTKAyYbqZag%3D%3D"
        SubInfo["Codes"] = api.wpdes(Ecode,deskey)
        x5 = api.getapi('UpdateSubInfoV2',SubInfo,key)  #修改支付订单
        paycode = {}
        paycode["UnionPayTradeNoOuter"] =  x4['OutputData'][0]["Data"][0]["UnionPayTradeNoOuter"]
        paycode["OrderID"] = x4['OutputData'][0]["Data"][0]["OrderID"]
        x6=api.getapi('UnionPayUseCode',paycode,key)
    return CinemaID,ScreeningPlanNo

getsea(10)