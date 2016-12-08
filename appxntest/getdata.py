#coding=utf-8
#import apitest
#import requests
#def getfilm():   #GetFilmHotAndReflected    获取待映影片列表
#def filmdata():  #GetFilmShowDateList   获取影片放映日期
#def GetCinema():   #GetFilmToCinemaList  获取影片放映影院列表
import userdata

class film():
    def __init__(self):
        self.cityID="1"
        self.CinemaID=userdata.CinemaID[userdata.jsq]
        self.username = userdata.username
        self.userid = userdata.userid
        self.password = userdata.password
        #username,userid,password = getuser(1)


    def GetFilmInfoToCinema(self):
        data={}
        data["CinemaID"] = self.CinemaID
        data['CityID']=self.cityID
        #{"InputData":[{"APIName":"GetFilmInfoToCinema","Parameters":[{"CinemaID":"2776","CityID":"1"}]}]}
        #{FilmID}
        return data

    def getGetScreeningPlanToCinema(self,FimlID):  #GetScreeningPlanToCinema  获取影片放映场次
        data={}
        data["CinemaID"]=self.CinemaID
        data['CityID']=self.cityID
        data['FimlID']=str(FimlID)
        #{"InputData":[{"APIName":"GetScreeningPlanToCinema","Parameters":[{"CinemaID":"2776","CityID":"1","FimlID":"26064"}]}]}
        return data#,ScreeningPlanNo

    def GetSeatList(self,ScreeningPlanNo):   #获取影片座位图
        data={}
        data["CinemaID"]=self.CinemaID
        data['ScreeningPlanNo']=ScreeningPlanNo
        #SeatID,SeatName,SeatState
        return data
    #{"InputData":[{"APIName":"GetSeatList","Parameters":[{"CinemaID":"2776","ScreeningPlanNo":"71327408"}]}]}

    def CreateSubscript(self,Mobile,SeatID,SeatName,SeatState,jsq):  #创建影票订单
        data={}
        data["ChannelNo"]="0"
        data["CinemaID"]=self.CinemaID
        data['Mobile']=self.username[jsq]
        data["PayType"] = "5"
        data["SeatInfo"] = SeatID
        data["SeatName"] = SeatName
        data["UserID"] = self.userid[jsq]
        data["Versions"] = "And4.3.5"
        return data
   # {"InputData":[{"APIName":"CreateSubscript","Parameters":[{"ChannelNo":"0","CinemaID":"2776","DeviceNumber":"f3d438a9ff853ec4f7331d2a8739af85",
    #"Mobile":"13693031400","PayType":"5","ScreeningPlanNo":"71327408","SeatInfo":"23858991|23858997|23858995|23858993|23858999",
   # "SeatName":"1:18|1:21|1:20|1:19|1:22","UserID":"2324531","Versions":"And4.3.5"}]}]}

    def getcard(self,jsq):  #CreateSubscript 获取用户卡信息
        data={}
        data["UserName"]=self.UserName[jsq]
        data["Password"]="ZIfEjSlihUhaXpAYafn7agJNNquwdyFHqocThLiFIuGHTKAyYbqZag\u003d\u003d\n"
        data['CityID']=self.cityID
        return data
        #CardNo
       # {"InputData":[{"APIName":"GetCardInfoV2","Parameters":
        #[{"CityID":"1","Password":"ZIfEjSlihUhaXpAYafn7agJNNquwdyFHqocThLiFIuGHTKAyYbqZag\u003d\u003d\n","UserName":"13693031400"}]}]}
    #def UpdateSubInfoV2  #联合支付

    #/AppInterface4.3.5/WebServiceV2.asmx/GetCinemaListV2    影院列表





