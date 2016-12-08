#coding=utf-8
#获取初始化用户信息以及影院信息
import data


x=1
jsq = 1
username,userid,password = data.getuser(x)
data=data.GetCinemaListV2(data.cityID)
x=data.getapi('GetCinemaListV2',data,data.key)
CinemaID=x['OutputData'][0]["Data"][jsq]["CinemaID"]


