#coding=utf-8
import requests
import os
import sqldate
import getdata
from data import *
from getdata import *


username,userid,password = getuser(1)
print(username,userid,password )



film = film.GetFilmInfoToCinema()  #获取影院ID
x1 = getapi('GetFilmInfoToCinema',film,key)
FilmID = ['OutputData'][0]["Data"][0]["FilmID"]

ScreeningPlan = film.getGetScreeningPlanToCinema(FilmID) #获取场次号
x1 = getapi('getGetScreeningPlanToCinema',ScreeningPlan,key)
ScreeningPlanNo = ['OutputData'][0]["Data"][0]["ScreeningPlanNo"]

seatlist = film.GetSeatList(ScreeningPlanNo)
x1 = getapi('GetSeatList',seatlist,key)
SeatID = ['OutputData'][0]["Data"][0]["SeatID"]
SeatName = ['OutputData'][0]["Data"][0]["SeatName"]
SeatState = ['OutputData'][0]["Data"][0]["SeatState"]

subscript =  film.CreateSubscript(SeatID,SeatName,SeatState)
x1 = getapi('CreateSubscript',seatlist,key)
SeatID = ['OutputData'][0]["Data"][0]["SeatID"]
