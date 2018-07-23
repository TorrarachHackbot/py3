# -*- coding: utf-8 -*-
from hackbot import *
from hack.ttypes import *
from hack.ttypes import Message
from hack.ttypes import ContentType as Type
from hack.ttypes import ChatRoomAnnouncementContents
from hack.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from ffmpy import FFmpeg
from humanfriendly import format_timespan, format_size, format_number, format_length
from subprocess import Popen, PIPE
import platform
import importlib
import html5lib,shutil
import wikipedia,goslate
import youtube_dl, pafy, asyncio
import time, timeit, base64, random, sys, json, codecs, threading, subprocess, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.request, urllib.parse, urllib.parse, traceback, atexit
_session = requests.session()
from gtts import gTTS
from googletrans import Translator

#==============================================================================#
botStart = time.time()
#==============================================================================#
#line = LINE()
line = LINE('EuRvOcMjvPHIRuHhE344.MTLqadV+ixwhpfd5+szaXa.7loVGJZe84J+Ko13/EdDHWIvTAn9CBffQ/F2kFhYoUI=')
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

#ki = LINE()
#ki = LINE('Eu9Fvv4TxTWO7mycjgE1.Db7+znDqi+c+Vn6qyTXniq.cG+WJM+4rTK/s/PoVs6Z3rdxEMrtd+CS6RDgNXTkwFo=')
#ki.log("Auth Token : " + str(ki.authToken))
#ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

#kk = LINE()
#kk = LINE('EukoXdcMhqJQeFYrlqm6.Tr9tg/NhW4W/V1OHe1YYrG.TDtkXqh9G4kIqfOx1HhmFIsazeZaUYsr+gCiPQO1moU=')
#kk.log("Auth Token : " + str(kk.authToken))
#kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

#kc = LINE()
#kc = LINE('EuJR2M8toPFA9OfkTMQ8.3AsVX43vq/7pg/mNMjDLoa.EnJfwLimw+HC+AIsM4r8Y4tAOVypuivKGhpM3AD7G4Q=')
#kc.log("Auth Token : " + str(kc.authToken))
#kc.log("Timeline Token : " + str(kc.tl.channelAccessToken))

#ke = LINE()
#ke = LINE('EuE1KNtMm7xEMQamE2cf.MaHMLBRN71LSwJF2ToAJpW.JshaI9FUefk7M8P7MKx/uNH+y1mvC6uXygswNGvCZos=')
#ke.log("Auth Token : " + str(ke.authToken))
#ke.log("Timeline Token : " + str(ke.tl.channelAccessToken))

#kr = LINE('EukGwCQDezx47egB1q54.WEdxqzuIkEaQi8BqMa0xPa.lnaAziIOTY12KFnbuhj9lYOktpqs7QRxhdgYgrSBIRc=')
#kr.log("Auth Token : " + str(kr.authToken))
#kr.log("Timeline Token : " + str(kr.tl.channelAccessToken))

print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

#kiMID = ki.profile.mid
#kiProfile = ki.getProfile()
#kiSettings = ki.getSettings()

#kkMID = kk.profile.mid
#kkProfile = kk.getProfile()
#kkSettings = kk.getSettings()

#kcMID = kc.profile.mid
#kcProfile = kc.getProfile()
#kcSettings = kc.getSettings()

#keMID = kc.profile.mid
#keProfile = kc.getProfile()
#keSettings = kc.getSettings()

#krMID = kc.profile.mid
#krprofile = kc.getProfile()
#krSettings = kc.getSettings()

#oepoll = OEPoll(ke)
#oepoll = OEPoll(kc)
#oepoll = OEPoll(kk)
#oepoll = OEPoll(ki)
oepoll = OEPoll(line)
#call = Call(line)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line]
#Exc = [ki,kk,kc,ke]
lineMID = line.getProfile().mid
#kiMID = ki.getProfile().mid
#kkMID = kk.getProfile().mid
#kcMID = kc.getProfile().mid
#kcMID = ke.getProfile().mid
#kcMID = kr.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["u9ad950003bff2175873c50f9fd2640c4",lineMID]
admin=['u9ad950003bff2175873c50f9fd2640c4',lineMID]
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#
settings = {
    "autoAdd": False,
    "autoJoin": True,
    'autoCancel':{"on":False,"members":10},	
    "autoLeave": False,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": False,
    "checkSticker": False,
    "kickMention": False,
    "potoMention": False,
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message":"✨ I love you ✨",
    "comment":"Thanks for add me",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": False,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke","บิน",".???","งงไปดิ","บินไปดิ","เซลกากจัง","@พี่อาร์ท","@ATR","ขอคลิปหน่อยครับ"]

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
 
def myhelp():
    myHelp = "╭══ ✨✨✨вотʟιиє ✮  " + "\n" \
                  "║ðﾟﾒﾥสถานะ" + "\n" + \
                  "║ðﾟﾒﾥคำสั่ง" + "\n" + \
                  "║ðﾟﾒﾥคำสั่ง1" + "\n" + \
                  "║ðﾟﾒﾥคำสั่ง2" + "\n" + \
                  "║ðﾟﾒﾥคำสั่ง3" + "\n" + \
                  "║ðﾟﾒﾥคำสั่ง4" + "\n" + \
                  "║ðﾟﾒﾥคำสั่ง5" + "\n" + \
                  "║ðﾟﾒﾥคำสั่ง6" + "\n" + \
                  "║ðﾟﾒﾥคท" + "\n" + \
                  "║ðﾟﾒﾥMymid" + "\n" + \
                  "║ðﾟﾒﾥชื่อ" + "\n" + \
                  "║ðﾟﾒﾥตัส" + "\n" + \
                  "║ðﾟﾒﾥรูป" + "\n" + \
                  "║ðﾟﾒﾥปก" + "\n" + \
                  "║ðﾟﾒﾥวีดีโอ" + "\n" + \
                  "║ðﾟﾒﾥMid" + "\n" + \
                  "║ðﾟﾒﾥName" + "\n" + \
                  "║ðﾟﾒﾥBio" + "\n" + \
                  "║ðﾟﾒﾥPict" + "\n" + \
                  "║ðﾟﾒﾥCover" + "\n" + \
                  "║ðﾟﾒﾥVideo" + "\n" + \
                  "║ðﾟﾒﾥCopy" + "\n" + \
                  "║ðﾟﾒﾥRestore" + "\n" + \
                  "║ðﾟﾒﾥMimic on/off" + "\n" + \
                  "║ðﾟﾒﾥMimicList" + "\n" + \
                  "║ðﾟﾒﾥMimicAdd" + "\n" + \
                  "║ðﾟﾒﾥMimicDel" + "\n" + \
                  "║ðﾟﾒﾥBroadcastvoice" + "\n" + \
                  "║ðﾟﾒﾥCbroadcastvoice" + "\n" + \
                  "║ðﾟﾒﾥRestart" + "\n" + \
                  "║ðﾟﾒﾥออน" + "\n" + \
                  "╰════"
    return myHelp

def listgrup():
    listGrup = "╭════HelpGroup " + "\n" + \
                  "║GroupCreator" + "\n" + \
                  "║GroupId" + "\n" + \
                  "║GroupName" + "\n" + \
                  "║GroupPicture" + "\n" + \
                  "║GroupList" + "\n" + \
                  "║GroupMemberList" + "\n" + \
                  "║GroupInfo" + "\n" + \
                  "║Url" + "\n" + \
                  "║Link on/off" + "\n" + \
                  "║Gurl" + "\n" + \
                  "║Friendlist" + "\n" + \
                  "║Blocklist" + "\n" + \
                  "║Friendlist mid" + "\n" + \
                  "║Invite:gcreator" + "\n" + \
                  "║Spam on/off" + "\n" + \
                  "║Reject inv" + "\n" + \
                  "║Allban" + "\n" + \
                  "║Grouplist" + "\n" + \
                  "║Blist" + "\n" + \
                  "║Mention" + "\n" + \
                  "║Lurking on" + "\n" + \
                  "║Lurking off" + "\n" + \
                  "║Lurking reset" + "\n" + \
                  "║Lurking" + "\n" + \
                  "║Invite" + "\n" + \
                  "║uninstall" + "\n" + \
                  "║Kick" + "\n" + \
                  "║Ban:on" + "\n" + \
                  "║Unban:on" + "\n" + \
                  "╰════"
    return listGrup

def socmedia():
    socMedia = "╭════✮ ғ✨✨✨✮" + "\n" + \
                  "║Instagram" + "\n" + \
                  "║Fotoig" + "\n" + \
                  "║Youtube" + "\n" + \
                  "║Music" + "\n" + \
                  "║Lyric" + "\n" + \
                  "║ScreenshootWebsite" + "\n" + \
                  "║Film:" + "\n" + \
                  "║Kalender" + "\n" + \
                  "║CheckDate" + "\n" + \
                  "║Textig" + "\n" + \
                  "║Wikipedia" + "\n" + \
                  "║Urban" + "\n" + \
                  "║Anime" + "\n" + \
                  "║Image" + "\n" + \
                  "║Pornhub" + "\n" + \
                  "╰════"
    return socMedia
    
def helpset():
    helpSet = "╭════HelpMySet " + "\n" + \
    "║ðﾟﾒﾥᴍʏ sᴇʟғ" + "\n" + \
    "║ðﾟﾒﾥsᴏᴄᴍᴇᴅɪᴀ" + "\n" + \
    "║ðﾟﾒﾥʟɪsᴛ ɢʀᴜᴘ" + "\n" + \
    "║ðﾟﾒﾥʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ" + "\n" + \
    "║ðﾟﾒﾥʟɪsᴛ ᴋɪᴄᴋᴇʀ" + "\n" + \
    "║ðﾟﾒﾥsᴛᴀᴛᴜs" + "\n" + \
    "║ðﾟﾒﾥᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ" + "\n" + \
    "║ðﾟﾒﾥʟɪsᴛ ᴛʀᴀɴsʟᴀᴛᴇ" + "\n" + \
    "╰════"
    return helpSet 

def helpkicker():
    helpKicker = "╭════ðﾟﾔﾘคำสั่งเตะต่างๆðﾟﾔﾘ" + "\n" + \
    "║ðﾟﾒﾥK1 kick" + "\n" + \
    "║ðﾟﾒﾥK2 kick" + "\n" + \
    "║ðﾟﾒﾥK3 kick" + "\n" + \
    "║ðﾟﾒﾥK1 invite" + "\n" + \
    "║ðﾟﾒﾥK2 inv" + "\n" + \
    "║ðﾟﾒﾥK3 vit" + "\n" + \
    "║ðﾟﾒﾥK1 tag" + "\n" + \
    "║ðﾟﾒﾥK1gruplist" + "\n" + \
    "║ðﾟﾒﾥK2listgrup" + "\n" + \
    "║ðﾟﾒﾥK3listrom" + "\n" + \
    "║ðﾟﾒﾥCleanse" + "\n" + \
    "║ðﾟﾒﾥScan blacklist" + "\n" + \
    "║ðﾟﾒﾥcb" + "\n" + \
    "║ðﾟﾒﾥNameall:" + "\n" + \
    "║ðﾟﾒﾥBioall" + "\n" + \
    "╰════"
    return helpKicker
    
def helpsetting():
    helpSetting = "╭════☣ตั้งค่าออโต้บลอค☣" + "\n" + \
    "║ðﾟﾒﾥProtect on/off" + "\n" + \
    "║ðﾟﾒﾥCancel pro on/off" + "\n" + \
    "║ðﾟﾒﾥInvit pro on/off" + "\n" + \
    "║ðﾟﾒﾥLink pro on/off" + "\n" + \
    "║ðﾟﾒﾥJoin pro on/off" + "\n" + \
    "║ðﾟﾒﾥProall on/off" + "\n" + \
    "║ðﾟﾒﾥAutojoin on/off" + "\n" + \
    "║ðﾟﾒﾥ""เปิด / ปิด กันรัน" + "\n" + \
    "║ðﾟﾒﾥAutoleave on/off" + "\n" + \
    "║ðﾟﾒﾥAutoread on/off" + "\n" + \
    "║ðﾟﾒﾥTag on/off" + "\n" + \
    "║ðﾟﾒﾥSelfbot on/off" + "\n" + \
    "║ðﾟﾒﾥTag2 on/off" + "\n" + \
    "║ðﾟﾒﾥChecksticker on/off" + "\n" + \
    "║ðﾟﾒﾥSider on/off" + "\n" + \
    "║ðﾟﾒﾥWelcomemessage on/off" + "\n" + \
    "║ðﾟﾒﾥLeavemessage on/off" + "\n" + \
    "╰════"
    return helpSetting

def helptexttospeech():
    helpTextToSpeech =   "╔══════════════┓" + "\n" + \
                         "╠⌬ ✰self protect✰    ⌬" + "\n" + \
                         "╚══════════════┛" + "\n" + \
                         "────┅═ই۝ई═┅────" + "\n" + \
                         "          ʜᴇʟᴘ ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ" + "\n" + \
                         "────┅═ই۝ई═┅────" + "\n" + \
                         "╔══════════════┓" + "\n" + \
                         "╠❂ af : Afrikaans" + "\n" + \
                         "╠❂ sq : Albanian" + "\n" + \
                         "╠❂ ar : Arabic" + "\n" + \
                         "╠❂ hy : Armenian" + "\n" + \
                         "╠❂ bn : Bengali" + "\n" + \
                         "╠❂ ca : Catalan" + "\n" + \
                         "╠❂ zh : Chinese" + "\n" + \
                         "╠❂ zh-cn : Chinese (Mandarin/China)" + "\n" + \
                         "╠❂ zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "╠❂ zh-yue : Chinese (Cantonese)" + "\n" + \
                         "╠❂ hr : Croatian" + "\n" + \
                         "╠❂ cs : Czech" + "\n" + \
                         "╠❂ da : Danish" + "\n" + \
                         "╠❂ nl : Dutch" + "\n" + \
                         "╠❂ en : English" + "\n" + \
                         "╠❂ en-au : English (Australia)" + "\n" + \
                         "╠❂ en-uk : English (United Kingdom)" + "\n" + \
                         "╠❂ en-us : English (United States)" + "\n" + \
                         "╠❂ eo : Esperanto" + "\n" + \
                         "╠❂ fi : Finnish" + "\n" + \
                         "╠❂ fr : French" + "\n" + \
                         "╠❂ de : German" + "\n" + \
                         "╠❂ el : Greek" + "\n" + \
                         "╠❂ hi : Hindi" + "\n" + \
                         "╠❂ hu : Hungarian" + "\n" + \
                         "╠❂ is : Icelandic" + "\n" + \
                         "╠❂ id : Indonesian" + "\n" + \
                         "╠❂ it : Italian" + "\n" + \
                         "╠❂ ja : Japanese" + "\n" + \
                         "╠❂ km : Khmer (Cambodian)" + "\n" + \
                         "╠❂ ko : Korean" + "\n" + \
                         "╠❂ la : Latin" + "\n" + \
                         "╠❂ lv : Latvian" + "\n" + \
                         "╠❂ mk : Macedonian" + "\n" + \
                         "╠❂ no : Norwegian" + "\n" + \
                         "╠❂ pl : Polish" + "\n" + \
                         "╠❂ pt : Portuguese" + "\n" + \
                         "╠❂ ro : Romanian" + "\n" + \
                         "╠❂ ru : Russian" + "\n" + \
                         "╠❂ sr : Serbian" + "\n" + \
                         "╠❂ si : Sinhala" + "\n" + \
                         "╠❂ sk : Slovak" + "\n" + \
                         "╠❂ es : Spanish" + "\n" + \
                         "╠❂ es-es : Spanish (Spain)" + "\n" + \
                         "╠❂ es-us : Spanish (United States)" + "\n" + \
                         "╠❂ sw : Swahili" + "\n" + \
                         "╠❂ sv : Swedish" + "\n" + \
                         "╠❂ ta : Tamil" + "\n" + \
                         "╠❂ th : Thai" + "\n" + \
                         "╠❂ tr : Turkish" + "\n" + \
                         "╠❂ uk : Ukrainian" + "\n" + \
                         "╠❂ vi : Vietnamese" + "\n" + \
                         "╠❂ cy : Welsh" + "\n" + \
                         "╚══════════════┛" + "\n" + "\n\n" + \
                          "「Contoh :✮ ғc.ρ'ʟιкнιт  вотʟιиє ✮ "
    return helpTextToSpeech
    
def helplanguange():
    helpLanguange =    "╔══════════════┓" + "\n" + \
                       "╠⌬ ғc.ρ'ʟιкнιт  вотʟιиє ✮ " + "\n" + \
                       "╚══════════════┛" + "\n" + \
                       "────┅═ই۝ई═┅────" + "\n" + \
                       "          ʜᴇʟᴘ ᴛʀᴀɴsʟᴀᴛᴇ" + "\n" + \
                       "────┅═ই۝ई═┅────" + "\n" + \
                       "╔══════════════┓" + "\n" + \
                       "╠❂ af : afrikaans" + "\n" + \
                       "╠❂ sq : albanian" + "\n" + \
                       "╠❂ am : amharic" + "\n" + \
                       "╠❂ ar : arabic" + "\n" + \
                       "╠❂ hy : armenian" + "\n" + \
                       "╠❂ az : azerbaijani" + "\n" + \
                       "╠❂ eu : basque" + "\n" + \
                       "╠❂ be : belarusian" + "\n" + \
                       "╠❂ bn : bengali" + "\n" + \
                       "╠❂ bs : bosnian" + "\n" + \
                       "╠❂ bg : bulgarian" + "\n" + \
                       "╠❂ ca : catalan" + "\n" + \
                       "╠❂ ceb : cebuano" + "\n" + \
                       "╠❂ ny : chichewa" + "\n" + \
                       "╠❂ zh-cn : chinese (simplified)" + "\n" + \
                       "╠❂ zh-tw : chinese (traditional)" + "\n" + \
                       "╠❂ co : corsican" + "\n" + \
                       "╠❂ hr : croatian" + "\n" + \
                       "╠❂ cs : czech" + "\n" + \
                       "╠❂ da : danish" + "\n" + \
                       "╠❂ nl : dutch" + "\n" + \
                       "╠❂ en : english" + "\n" + \
                       "╠❂ eo : esperanto" + "\n" + \
                       "╠❂ et : estonian" + "\n" + \
                       "╠❂ tl : filipino" + "\n" + \
                       "╠❂ fi : finnish" + "\n" + \
                       "╠❂ fr : french" + "\n" + \
                       "╠❂ fy : frisian" + "\n" + \
                       "╠❂ gl : galician" + "\n" + \
                       "╠❂ ka : georgian" + "\n" + \
                       "╠❂ de : german" + "\n" + \
                       "╠❂ el : greek" + "\n" + \
                       "╠❂ gu : gujarati" + "\n" + \
                       "╠❂ ht : haitian creole" + "\n" + \
                       "╠❂ ha : hausa" + "\n" + \
                       "╠❂ haw : hawaiian" + "\n" + \
                       "╠❂ iw : hebrew" + "\n" + \
                       "╠❂ hi : hindi" + "\n" + \
                       "╠❂ hmn : hmong" + "\n" + \
                       "╠❂ hu : hungarian" + "\n" + \
                       "╠❂ is : icelandic" + "\n" + \
                       "╠❂ ig : igbo" + "\n" + \
                       "╠❂ id : indonesian" + "\n" + \
                       "╠❂ ga : irish" + "\n" + \
                       "╠❂ it : italian" + "\n" + \
                       "╠❂ ja : japanese" + "\n" + \
                       "╠❂ jw : javanese" + "\n" + \
                       "╠❂ kn : kannada" + "\n" + \
                       "╠❂ kk : kazakh" + "\n" + \
                       "╠❂ km : khmer" + "\n" + \
                       "╠❂ ko : korean" + "\n" + \
                       "╠❂ ku : kurdish (kurmanji)" + "\n" + \
                       "╠❂ ky : kyrgyz" + "\n" + \
                       "╠❂ lo : lao" + "\n" + \
                       "╠❂ la : latin" + "\n" + \
                       "╠❂ lv : latvian" + "\n" + \
                       "╠❂ lt : lithuanian" + "\n" + \
                       "╠❂ lb : luxembourgish" + "\n" + \
                       "╠❂ mk : macedonian" + "\n" + \
                       "╠❂ mg : malagasy" + "\n" + \
                       "╠❂ ms : malay" + "\n" + \
                       "╠❂ ml : malayalam" + "\n" + \
                       "╠❂ mt : maltese" + "\n" + \
                       "╠❂ mi : maori" + "\n" + \
                       "╠❂ mr : marathi" + "\n" + \
                       "╠❂ mn : mongolian" + "\n" + \
                       "╠❂ my : myanmar (burmese)" + "\n" + \
                       "╠❂ ne : nepali" + "\n" + \
                       "╠❂ no : norwegian" + "\n" + \
                       "╠❂ ps : pashto" + "\n" + \
                       "╠❂ fa : persian" + "\n" + \
                       "╠❂ pl : polish" + "\n" + \
                       "╠❂ pt : portuguese" + "\n" + \
                       "╠❂ pa : punjabi" + "\n" + \
                       "╠❂ ro : romanian" + "\n" + \
                       "╠❂ ru : russian" + "\n" + \
                       "╠❂ sm : samoan" + "\n" + \
                       "╠❂ gd : scots gaelic" + "\n" + \
                       "╠❂ sr : serbian" + "\n" + \
                       "╠❂ st : sesotho" + "\n" + \
                       "╠❂ sn : shona" + "\n" + \
                       "╠❂ sd : sindhi" + "\n" + \
                       "╠❂ si : sinhala" + "\n" + \
                       "╠❂ sk : slovak" + "\n" + \
                       "╠❂ sl : slovenian" + "\n" + \
                       "╠❂ so : somali" + "\n" + \
                       "╠❂ es : spanish" + "\n" + \
                       "╠❂ su : sundanese" + "\n" + \
                       "╠❂ sw : swahili" + "\n" + \
                       "╠❂ sv : swedish" + "\n" + \
                       "╠❂ tg : tajik" + "\n" + \
                       "╠❂ ta : tamil" + "\n" + \
                       "╠❂ te : telugu" + "\n" + \
                       "╠❂ th : thai" + "\n" + \
                       "╠❂ tr : turkish" + "\n" + \
                       "╠❂ uk : ukrainian" + "\n" + \
                       "╠❂ ur : urdu" + "\n" + \
                       "╠❂ uz : uzbek" + "\n" + \
                       "╠❂ vi : vietnamese" + "\n" + \
                       "╠❂ cy : welsh" + "\n" + \
                       "╠❂ xh : xhosa" + "\n" + \
                       "╠❂ yi : yiddish" + "\n" + \
                       "╠❂ yo : yoruba" + "\n" + \
                       "╠❂ zu : zulu" + "\n" + \
                       "╠❂ fil : Filipino" + "\n" + \
                       "╠❂ he : Hebrew" + "\n" + \
                       "╚══════════════┛" + "\n" + "\n\n" + \
                       "「Contoh : ✮ ғc.ρ'ʟιкнιт  вотʟιиє ✮ "
    return helpLanguange
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.blockContact(op.param1)
                ki.blockContact(op.param1)
                kk.blockContact(op.param1)
                kc.blockContact(op.param1)
                ke.blockContact(op.param1)
                kr.blockContact(op.param1)
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)				
#        if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
#        if op.type == 24:
#            if settings["autoLeave"] == True:
#                line.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if ".say " in msg.text.lower():
                    spl = re.split(".say ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == 'คำสั่ง':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == 'คำสั่ง2':
                    helpSet = helpset()
                    line.sendMessage(to, str(helpSet))
                    sendMessageWithMention(to, lineMID)
                elif text.lower() == 'คำสั่ง3':
                    helpKicker = helpkicker()
                    line.sendMessage(to, str(helpKicker))
                elif text.lower() == 'คำสั่ง4':
                    listGrup = listgrup()
                    line.sendMessage(to, str(listGrup))
                elif text.lower() == 'คำสั่ง5':
                    helpSetting = helpsetting()
                    line.sendMessage(to, str(helpSetting))
                elif text.lower() == 'คำสั่ง6':
                    socMedia = socmedia()
                    line.sendMessage(to, str(socMedia))
                elif text.lower() == 'คำสั่ง7':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'คำสั่ง8':
                    helpLanguange = helplanguange()
                    line.sendMessage(to, str(helpLanguange))
#==============================================================================#
                #elif text.lower() == 'speed':
                    #start = time.time()
                    #line.sendMessage(to, "✨•┅───┈ ")
                    #elapsed_time = time.time() - start
                    #line.sendMessage(msg.to, "✨ %s Se✨(elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "✨•┅───┈ ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Sec ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")						
                elif text.lower() == 'รีบอท':
                    line.sendMessage(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ ..")
                    line.sendMessage(to, "Success Restarting.")
                    restartBot()
                elif text.lower() == 'ออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "✨{}".format(str(runtime)))
                elif text.lower() == 'สถานะ':
                    try:
                        arr = []
                        owner = "u9ad950003bff2175873c50f9fd2640c4"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ คำสั่งลิขิตðﾟﾔﾞҨနနஅҨՁণюðﾟﾒﾞ"
                        ret_ += "\n╠۝ðﾟﾒﾘ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠۝ðﾟﾒﾘ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠۝ðﾟﾒﾘ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠۝ðﾟﾒﾘ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[สถานะ]"
                        ret_ += "\n╠۝ðﾟﾒﾘ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[✮ ғc.ρ'ʟιкнιт  вотʟιиє ✮ "
                        line.sendContact(to, owner)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔════[ Status ]═════┓"
                        if settings["autoAdd"] == True: ret_ += "\n╠ ðﾟﾒﾢรับแอดออโต้ ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥรับแอดออโต้    ✘ "
                        if settings["autoJoin"] == True: ret_ += "\n╠ ðﾟﾒﾢเข้าห้องออโต้ ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥเข้าห้องออโต้    ✘ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠ ðﾟﾒﾢยกเลิกเชิญกลุ่มเมื่ต่ำกว่า: " + str(settings["autoCancel"]["members"]) + " → ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥยกเลิกเชิญกลุ่ม    ✘ "						
                        if settings["autoLeave"] == True: ret_ += "\n╠ ðﾟﾒﾢออกแชทรวม ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥออกแชทรวม ✘ "
                        if settings["autoRead"] == True: ret_ += "\n╠ ðﾟﾒﾢอ่านออโต้ ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥอ่านออโต้   ✘ "				
                        if settings["checkSticker"] == True: ret_ += "\n╠ ðﾟﾒﾢSticker ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥSticker        ✘ "
                        if settings["detectMention"] == True: ret_ += "\n╠ ðﾟﾒﾢตอบกลับคนแทค ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥตอบกลับคนแทค ✘ "
                        if settings["potoMention"] == True: ret_ += "\n╠ ðﾟﾒﾢแสดงภาพคนแทค ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥแสดงภาพคนแทค ✘ "						
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠ ðﾟﾒﾢกันเชิญ ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥกันเชิญ ✘ "
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠ ðﾟﾒﾢกันยกเชิญ ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥกันยกเชิญ ✘ "
                        if RfuProtect["protect"] == True: ret_ += "\n╠ ðﾟﾒﾢป้องกัน ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥป้องกัน ✘ "
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠ ðﾟﾒﾢป้องกันเปิดลิ้ง ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥป้องกันเปิดลิ้ง ✘ "
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠ ðﾟﾒﾢป้องกันสมาชิก ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥป้องกันสมาชิก ✘ "
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠ ðﾟﾒﾢป้องกันเข้ากลุ่ม ✔"
                        else: ret_ += "\n╠ ðﾟﾒﾥป้องกันเข้ากลุ่ม ✘ "						
                        ret_ += "\n╚════[ Status ]═════┛"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == 'ปิด กันรัน':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "เปิดรับเพื่อนแล้ว")
                elif text.lower() == 'เปิด กันรัน':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "ðﾟﾑﾠปิด เพิ่มเพื่อนแล้วðﾟﾓ﾿")
                elif text.lower() == 'เปิด เข้ากลุ่ม':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "Autojoin ")
                elif text.lower() == 'ปิด เข้ากลุ่ม':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "ðﾟﾤﾗปิดเข้ากลุ่มแล้วðﾟﾘﾋ")
                elif "Gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,strnum + " สมาชิกในกลุ่มจะปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,"Value is wrong")
                        else:
                                line.sendText(msg.to,"Bizarre ratings")					
                elif text.lower() == 'Leave on':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "ออกจากแชทรวมแล้ว")
                elif text.lower() == 'Leave off':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "ออกแชทรวมปิด")
                elif text.lower() == 'Read on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "อ่านออโต้เปิดแล้ว")
                elif text.lower() == 'Read off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "อ่านออโต้ปิดแล้ว")
                elif text.lower() == 'sticker on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Check sticker enabled.")
                elif text.lower() == 'sticker off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Check sticker disabled.")                
#==============================================================================#
                elif text.lower() == 'มี':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == 'creator':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, "u9ad950003bff2175873c50f9fd2640c4")
                elif text.lower() == 'ไอดี':
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                elif text.lower() == 'ชื่อ':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[ชื่อเรา]\n" + me.displayName)
                elif text.lower() == 'ตัส':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[สถานะเรา]\n" + me.statusMessage)
                elif text.lower() == 'รูป':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'วีดีโอ':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'ปก':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("me "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("pict "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("video "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("copy "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            line.sendMessage(msg.to, "ðﾟﾘﾊðﾟﾘﾊ")
                        except:
                            line.sendMessage(msg.to, "ðﾟﾘﾊðﾟﾘﾊ")
                            
                elif text.lower() == 'backup':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        line.sendMessage(msg.to, "Berhasil restore profile")
                    except:
                        line.sendMessage(msg.to, "Gagal restore profile")
						
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")
#==============================================================================#
                elif text.lower() == 'ดูแอด':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "คนนี้สร้าðﾟﾘﾍ")
                elif text.lower() == 'groupid':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ID GROUP \n" + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "Group -> \n" + gid.name)
                elif text.lower() == 'url':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "Link Qr Group\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Link Qr to open")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "Link Qr to open")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Link Qr to closed.")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Link Qr to closed.")
                elif text.lower() == 'ดูกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลห้องðﾟﾘﾍ]"
                    ret_ += "\n╠ ðﾟﾒﾞชื่อห้อง: {}".format(str(group.name))
                    ret_ += "\n╠ ðﾟﾒﾞไอดีห้อง : {}".format(group.id)
                    ret_ += "\n╠ ðﾟﾒﾞผู้สร้าง : {}".format(str(gCreator))
                    ret_ += "\n╠ ðﾟﾒﾞสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ ðﾟﾒﾞค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ðﾟﾒﾞคิวอาร์โค๊ต : {}".format(gQr)
                    ret_ += "\n╠ ðﾟﾒﾞลิ้งห้อง : {}".format(gTicket)
                    ret_ += "\n╚══[ สิ้นสุด]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'สมาชิก':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ สมาชิกทั้งหมด]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'ลิสกลุ่ม':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))

                elif text.lower() == 'k1gruplist':
                        groups = ki.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ki.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        ki.sendMessage(to, str(ret_))

                elif text.lower() == 'k2listgrup':
                        groups = kk.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = kk.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        kk.sendMessage(to, str(ret_))

                elif text.lower() == 'k3listroom':
                        groups = kc.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = kc.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        kc.sendMessage(to, str(ret_))
						
                elif text.lower() == 'k4listroom':
                        groups = ke.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ke.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        ke.sendMessage(to, str(ret_))					
                elif "มาโทร" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"เชิญเข้าร่วมการโทรสำเร็จ(｀・ω・´)")	
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass	
                elif msg.text.lower() == ".getjoined":
                    line.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = line.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += line.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            line.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    line.sendText(msg.to,text[:-2])
                    cnt = 0				
                elif ".info " in msg.text.lower():
                    spl = re.split(".info ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = line.getContact(uid)
                            try:
                                line.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+userData.pictureStatus)
                            except:
                                pass
                            line.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            line.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            line.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)
                            msg.contentType = 13
                            msg.text = None
                            msg.contentMetadata = {'mid': userData.mid}
                            line.sendMessage(msg)
                elif "ลิขิต" in msg.text:
                    spl = msg.text.split("ลิขิต")
                    if spl[len(spl)-1] == "":
                        line.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)	
                elif ".denyall" in msg.text.lower():
                    spl = re.split(".denyall",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendText(msg.to,"สำเร็จแล้ว")	
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        line.sendMessage(msg)
                elif ".remove " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                elif ".bye " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == ".myid":
                    line.sendText(msg.to,user1)
                elif msg.text.lower().startswith("yo!!"):
                    data = msg.text[len("yo!!"):].strip()
                    if data == "":
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "+":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count > mentargs:
                                break
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == ">":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        if mentargs >= 0:
                            strt = len(str(mentargs)) + 2
                        else:
                            strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count < mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "=":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count != mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            strt = len(str(count)) + 2
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                elif ".tx " in msg.text.lower():
                    spl = re.split(".tx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        line.kedapkedip(msg.to,spl[1])
                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".nmx " in msg.text.lower():
                    spl = re.split(".nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = line.nmxstring(spl[1])
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".join " in msg.text.lower():
                    spl = re.split(".join ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendText(msg.to,str(e))	
                elif msg.text.lower().startswith(".ctt "):
                    try:
                        text = msg.text.split(" ",1)[1]
                        headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                        }
                        data = {
                        "q":text
                        }
                        conv = BeautifulSoup(requests.post("http://lullar-de-2.appspot.com/",headers=headers,data=data).content,"html.parser").find("span",attrs={"style":"font-size:40px"}).text
                        if msg.toType != 0:
                                kk.sendText(msg.to,"Conversion:\n"+conv)
                        else:
                                kk.sendText(msg.from_,"Conversion:\n"+conv)
                    except Exception as e:
                        print(e)						
                elif msg.text.lower().startswith("pz:gac "):
                    pnum = re.split("pz:gac ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                kk.sendText(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                kk.sendText(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                kk.sendText(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                kk.sendText(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                kk.sendText(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                kk.sendText(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg.to)))
                    else:
                        line.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            line.sendText(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")

                if msg.text.lower() == ".me":
                    msg.contentType = 13
                    msg.text = None
                    msg.contentMetadata = {'mid': user1}
                    line.sendMessage(msg)
                if msg.text.lower() == ".gift":
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)
                if ".gift " in msg.text.lower():
                    red = re.compile(re.escape('.gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)						
#==============================================================================#
                elif text.lower() == 'ทท':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//500
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*500 : (a+1)*500]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "จำนวน {} คน".format(str(len(nama))))          

                elif text.lower() == 'k1 tag':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members if contact.mid != lineMID]
                    k = len(nama)//500
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*500 : (a+1)*500]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        ki.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        ki.sendMessage(to, "จำนวน {} คน".format(str(len(nama))))          

                elif text.lower() == 'แอบ':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา: [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "เริ่มจับเวลา:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking disabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'อ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ **คนที่แอบอ่าน** ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ เวลาที่อ่าน ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")	
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)

                elif msg.text in ["Jumanji"]:
                    hasil = "https://youtu.be/2QKg5SZ_35I"
                    A = hasil
                    line.sendVideoWithURL(msg.to, A)

#sender = msg._from
#            if msg.toType == 0:
#                if sender != line.profile.mid:
#==============================================================================#   
                elif "Broadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Bcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Cbroadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Cbcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Wikipedia " in msg.text:
                      try:
                          wiki = msg.text.lower().replace("Wikipedia ","")
                          wikipedia.set_lang("id")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          line.sendMessage(msg.to, pesan)
                      except:
                              try:
                                  pesan="Over Text Limit! Please Click link\n"
                                  pesan+=wikipedia.page(wiki).url
                                  line.sendText(msg.to, pesan)
                              except Exception as e:
                                  line.sendMessage(msg.to, str(e))

                elif "Film:" in msg.text:
                    proses = msg.text.split(":")
                    get = msg.text.replace(proses[0] + ":","")
                    getfilm = get.split()
                    title = getfilm[0]
                    tahun = getfilm[1]
                    r = requests.get('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                    start = time.time()
                    data=r.text
                    data=json.loads(data)
                    hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                    hasil += "\n\n " +str(data["Plot"])
                    hasil += "\n\nDirector : " +str(data["Director"])
                    hasil += "\nActors   : " +str(data["Actors"])
                    hasil += "\nRelease : " +str(data["Released"])
                    hasil += "\nGenre    : " +str(data["Genre"])
                    hasil += "\nRuntime   : " +str(data["Runtime"])
                    path = data["Poster"]
                    line.sendImageWithURL(msg.to, str(path))
                    line.sendMessage(msg.to,hasil)

                elif text.lower() == 'ปฏิทิน':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        line.sendImageWithURL(to, data["result"])
                elif "วันนี้" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    line.sendMessage(to, str(ret_))
                
                elif "อิน" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ จำนวน Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Pengguna tidak ditemukan")
                elif "fotoig" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1):
                            print(('send foto : ', count))
                            r = x.get(profile, params={'max_id': end_cursor})                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                print((node['display_src']))
                                line.sendImageWithURL(msg.to,node['display_src'])
                elif "ภาพ" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "อะนิเมะ" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "Youtube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผมการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif msg.text in ["Cctv on"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"Cctv on Ready")
                elif msg.text in ["Cctv off"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "Cctv Already Off")

                elif text.lower() == 'selfbot off':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)

                elif text.lower() == 'เพื่อน':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="ðﾟﾎﾎList Friendðﾟﾎﾎ"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\nðﾟﾎﾎList Friendðﾟﾎﾎ\n\nTotal Teman : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["Blocklist"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════Daftar Akun Yang di Blocked═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════List Blocked════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["Friendlist mid"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════List FriendMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text.lower() == 'gurl':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link Groupnya Tanpa Buka Qr\n╚══════════════┛")

                elif msg.text == "Pornhub":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")

                elif msg.text.lower() == 'invite:gcreator':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Typeðﾟﾑﾉ Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["/uninstall"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)
                            ki.leaveGroup(receiver)
                            kk.leaveGroup(receiver)
                            kc.leaveGroup(receiver)
                            ke.leaveGroup(receiver)							
                        except:
                            pass

                elif msg.text in ["Tagimage on","Tag2 on"]:
                        settings['potoMention'] = True
                        line.sendMessage(msg.to,"เปิดตอบกลัภาะบแล้ว")
                
                elif msg.text in ["Tagimage off","Tag2 off"]:
                        settings['potoMention'] = False
                        line.sendMessage(msg.to,"ปิดตอบกลับแล้ว")

                elif msg.text in ["Respontag on","Tag on","My respon on","Respon:on"]:
                    settings["detectMention"] = True
                    line.sendMessage(msg.to,"ตอบกลับอัตโนมัติแล้ว")
                
                elif msg.text in ["Respontag off","Tag off","My respon off","Respon:off"]:
                    settings["detectMention"] = False
                    line.sendMessage(msg.to,"ปิดตอบกลับอัตโนมัติแล้ว")

                elif msg.text.lower().startswith("textig "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)

                elif "kedip " in msg.text:
                    txt = msg.text.replace("kedip ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    line.sendMessage(msg.to, t1 + txt + t2)						
                elif msg.text in ["บอท1ลบสิริ"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki.getGroup(msg.to)
                        if kiMID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki.sendText(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
										
                elif msg.text in ["บอท2ลบสิริ"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = kk.getGroup(msg.to)
                        if kkMID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                kk.sendText(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    kk.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                elif msg.text in ["บอท3ลบสิริ"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = kc.getGroup(msg.to)
                        if kcMID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                kc.sendText(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    kc.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                elif msg.text in ["บอท4ลบสิริ"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ke.getGroup(msg.to)
                        if kcMID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ke.sendText(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    ke.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass									
                elif msg.text in ["Inviteuser"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"send a contact to invite user")                            
                elif msg.text.lower() == ".invitecancel":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == ".invitecancel2":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == "ออน":
                    line.sendText(msg.to,(str(datetime.datetime.now() - start_runtime)[:-7].split(" days, ")[0]+" วัน "+str(datetime.datetime.now() - start_runtime)[:-7].split(" days, ")[1].split(":")[0]+" ชั่วโมง " if "days" in str(datetime.datetime.now() - start_runtime) else str(datetime.datetime.now() - start_runtime)[:-7].split(" day, ")[0]+" วัน "+str(datetime.datetime.now() - start_runtime)[:-7].split(" day, ")[1].split(":")[0]+" ชั่วโมง " if "day" in str(datetime.datetime.now() - start_runtime) else str(datetime.datetime.now() - start_runtime)[:-7].split(":")[0]+" ชั่วโมง ")+str(datetime.datetime.now() - start_runtime)[:-7].split(":")[1]+" นาที "+str(datetime.datetime.now() - start_runtime)[:-7].split(":")[2]+" วินาที")
#=============COMMAND KICKER===========================#
                elif msg.text in ["cb"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลบัญชีดำทั้งหมดเรียร้อย")
                    print ("Clear Ban")

                elif text.lower() == 'มม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        group.preventedJoinByTicket = False
                        line.updateGroup(group)
                        invsend = 0
                        ticket = line.reissueGroupTicket(to)
                        ki.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kr.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        group.preventedJoinByTicket = True
                        line.updateGroup(group)
                        print ("Kicker Join")

                elif 'yk' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(Rfu).kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               random.choice(Rfu).sendMessage(msg.to,"Limit kaka ðﾟﾘﾫ")

                elif 'kill' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka ðﾟﾘﾫ")                               

                elif 'y1' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki.kickoutFromGroup(msg.to,[target])           
                               print ("K1 Kick User")
                           except:
                               ki.sendMessage(msg.to,"Limit kaka ðﾟﾘﾫ")                               

                elif 'y2' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kk.kickoutFromGroup(msg.to,[target])
                               print ("K2 kick user")
                           except:
                               kk.sendMessage(msg.to,"Limit kaka ðﾟﾘﾫ")                              

                elif 'y3' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kc.kickoutFromGroup(msg.to,[target])
                               print ("K3 kick user")
                           except:
                               kc.sendMessage(msg.to,"Limit kaka ðﾟﾘﾫ")                              

                elif 'y4' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ke.kickoutFromGroup(msg.to,[target])
                               print ("K3 kick user")
                           except:
                               ke.sendMessage(msg.to,"Limit kaka ðﾟﾘﾫ")                              
                               
                elif 'invite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "Typeðﾟﾑﾉ Invite Succes")
                           except:
                               line.sendMessage(msg.to,"Typeðﾟﾑﾉ Limit Invite")

                elif 'k1 invite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki.inviteIntoGroup(msg.to,[target])
                               ki.sendMessage(receiver, "Typeðﾟﾑﾉ Invite Succes")
                               print ("R1 invite User")
                           except:
                               ki.sendMessage(msg.to,"Typeðﾟﾑﾉ Limit Invite")                               

                elif 'k2 inv' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kk.inviteIntoGroup(msg.to,[target])
                               kk.sendMessage(receiver, "Typeðﾟﾑﾉ Invite Succes")
                               ("R2 invite User")
                           except:
                               kk.sendMessage(msg.to,"Typeðﾟﾑﾉ Limit Invite")                               

                elif 'k3 getinvite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kc.inviteIntoGroup(msg.to,[target])
                               kc.sendMessage(receiver, "Typeðﾟﾑﾉ Invite Succes")
                               ("R3 invite User")
                           except:
                               kc.sendMessage(msg.to,"Typeðﾟﾑﾉ Limit Invite")                               

                elif 'k4 getinvite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ke.inviteIntoGroup(msg.to,[target])
                               ke.sendMessage(receiver, "Typeðﾟﾑﾉ Invite Succes")
                               ("R4 invite User")
                           except:
                               ke.sendMessage(msg.to,"Typeðﾟﾑﾉ Limit Invite")                               

                elif "Cleanse" in msg.text:
                	if msg.toType == 2:
                         _name = msg.text.replace("Cleanse","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"Just some casual cleansing ô")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"Not found.")
                         else:
                             for target in targets:
                             	if not target in Rfu:
                                     try:
                                         klist=[line,ki,kk,kc,ke]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"Group cleanse")
                                         print ("Cleanse Group")

                elif msg.text in ["Scan blacklist"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"Nots in Blacklist")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line,ki,kk,kc,ke]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")

                elif text.lower() == "removechat":
                        if msg._from in Family:
                            try:
                                ki.removeAllMessages(op.param2)
                                kk.removeAllMessages(op.param2)
                                kc.removeAllMessages(op.param2)
                                ke.removeAllMessages(op.param2)                                
                                line.sendMessage(msg.to,"Remove chat Kicker success....")
                            except:
                                pass
                                print ("Remove Chat Kicker")

                elif text.lower() == "บบ":
                    if msg._from in Family:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        kr.leaveGroup(msg.to)
                        print ("Kicker Leave")

                elif text.lower() == "leaveall":
                    if msg._from in Family:
                        gid = line.getGroupIdsJoined()
                        for i in gid:
                            ki.leaveGroup(i)
                            kk.leaveGroup(i)
                            kc.leaveGroup(i)
                            ke.leaveGroup(i)                            
                            print ("Kicker Leave All group")

                elif "myname: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Update to " + string)
                        print ("Update Name")

                elif "upbio: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Succes Update ðﾟﾑﾉ " + string)
                        print ("Update Bio Succes")

                elif "nameall: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki.getProfile()
                        profile_B = kk.getProfile()
                        profile_C = kc.getProfile()
                        profile_D = ke.getProfile()                        
                        profile_A.displayName = string
                        profile_B.displayName = string
                        profile_C.displayName = string
                        profile_D.displayName = string                        
                        ki.updateProfile(profile_A)
                        kk.updateProfile(profile_B)
                        kc.updateProfile(profile_C)
                        ke.updateProfile(profile_D)                        
                        line.sendMessage(msg.to,"Update Name All Kicker to : " + string)
                        print ("Update Name All Kicker")

                elif "bioall: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki.getProfile()
                        profile_B = kk.getProfile()
                        profile_C = kc.getProfile()
                        profile_D = kc.getProfile()                        
                        profile_A.statusMessage = string
                        profile_B.statusMessage = string
                        profile_C.statusMessage = string
                        profile_D.statusMessage = string                        
                        ki.updateProfile(profile_A)
                        kk.updateProfile(profile_B)
                        kc.updateProfile(profile_C)
                        ke.updateProfile(profile_D)                        
                        line.sendMessage(msg.to,"Update Bio All Kicker to : " + string)
                        print ("Update Bio All Kicker")

                elif text.lower() == "รายงาน":
                    if msg._from in Family:
                        profile = ki.getProfile()
                        text = profile.displayName + "\nรายงานตัว"
                        ki.sendMessage(to, text)                                
                        profile = kk.getProfile()
                        text = profile.displayName + "\nรายงานตัว"
                        kk.sendMessage(to, text)                                
                        profile = kc.getProfile()
                        text = profile.displayName + "\nรายงานตัว"
                        kc.sendMessage(to, text)
                        profile = ke.getProfile()                        
                        text = profile.displayName + "\nรายงานตัว"
                        ke.sendMessage(to, text)                        
                        print ("Kicker Respon")

                elif msg.text in ["Bot?"]:
                    ki.sendMessage(msg.to,"พี่ลิขิตðﾟﾔﾞҨနနஅҨՁণюðﾟﾒﾞðﾟﾑﾀ❣")
                    kk.sendMessage(msg.to,"✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰2")
                    kc.sendMessage(msg.to,"✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰3")
                    ke.sendMessage(msg.to,"✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰4")    
                elif msg.text.lower().startswith("bitcoin"):
                   search = msg.text.split("bitcoin")
                   with requests.session() as web:
                       web.headers["User-Agent"] = random.choice(settings["userAgent"])
                       url = "https://xeonwz.herokuapp.com/bitcoin.api"
                       r = web.get(url)
                       data=r.text
                       data=json.loads(data)
                       print(data)
                       hasil = "「 Bitcoin Result 」"
                       hasil += "\nPrice : " +str(data["btc"])                                
                       hasil += "\nExpensive : " +str(data["high"])
                       hasil += "\nCheap : " +str(data["low"])               
                       line.sendMessage(to, str(hasil))
#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == 'protect on':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")

                elif msg.text.lower() == 'protect off':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")

                elif msg.text.lower() == 'Pro on':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'cancel pro off':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'invit pro on':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'invit pro off':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'link pro on':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'link pro off':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'guest pro on':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'guest pro off':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'join pro on':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'join pro off':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'proall on':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

                elif msg.text.lower() == 'proall off':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == 'คนเข้าเปิด':
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   .")
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")
                elif msg.text.lower() == 'คนเข้าปิด':
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")

                elif msg.text.lower() == 'k1 on':
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                elif msg.text.lower() == 'k1 off':
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")

                elif text.lower() == 'ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบรันเสร็จแล้วขอรับ")
                    line.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))								
								
                elif "Allban" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("Allban","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"Banned all")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"All members has been added ban.")
										   
                elif 'ban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes added for the blacklist ")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

                elif 'unban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes unban from the blacklist. ")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

                elif msg.text in ["เชคดำ"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่พบ") 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ติดดำ")
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
              
#==============================================================================#
        if op.type == 19:
          if op.param2 in Family:
            pass
          if op.param2 in RfuBot:
          	pass
          else:
            if op.param3 in lineMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kk.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kk.updateGroup(G)
                  ticket = kk.reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  line.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in kiMID:
              if op.param2 not in Family:
                try:
                  G = kk.getGroup(op.param1)
                  G = kc.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kc.updateGroup(G)
                  ticket = kc.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  kk.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kk.updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in kkMID:
              if op.param2 not in Family:
                try:
                  G = kc.getGroup(op.param1)
                  G = ki.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kc.updateGroup(G)
                  ticket = ki.reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  kk.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in kcMID:
              if op.param2 not in Family:
                try:
                  G = kk.getGroup(op.param1)
                  G = ke.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki.updateGroup(G)
                  ticket = ki.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  kc.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in keMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kc.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki.updateGroup(G)
                  ticket = ki.reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ke.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)                  

            if op.param3 in krMID:
              if op.param2 not in Family:
                try:
                  G = kk.getGroup(op.param1)
                  G = ke.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kk.updateGroup(G)
                  ticket = kk.reissueGroupTicket(op.param1)
                  kr.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  kr.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  kr.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)                  

        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)                
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)                
#==============================================================================#
        if op.type == 19:
            try:
                if op.param3 in lineMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                                                
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True                       

                elif op.param3 in kiMID:
                    if op.param2 in lineMID:
                        G = kk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in kkMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in kcMID:
                    if op.param2 in kkMID:
                        G = kk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                elif op.param3 in keMID:
                    if op.param2 in kcMID:
                        G = ke.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ke.updateGroup(G)
                        ticket = ke.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                    else:
                        G = ke.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ke.updateGroup(G)
                        ticket = ke.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ke.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                elif op.param3 in krMID:
                    if op.param2 in keMID:
                        G = kr.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kr.updateGroup(G)
                        ticket = ke.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        kr.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ke.updateGroup(G)
                    else:
                        G = kr.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kr.updateGroup(G)
                        ticket = kr.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        kr.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        kr.updateGroup(G)
                        settings["blacklist"][op.param2] = True
            except:
                pass
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])

        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))
                    ki.sendMessage(op.param1,str(settings["message"]))
                    kk.sendMessage(op.param1,str(settings["message"]))
                    kc.sendMessage(op.param1,str(settings["message"]))
                    ke.sendMessage(op.param1,str(settings["message"]))                    

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])                    

        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                    ki.sendChatChecked(to, msg_id)
                    kk.sendChatChecked(to, msg_id)
                    kc.sendChatChecked(to, msg_id)
                    ke.sendChatChecked(to, msg_id)					
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["『 Auto Respon』\n " + cName + "\n『แทคทำไมหรอ?』"]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)
                                          sendMessageWithMention(to, contact.mid)
                                          break										  
                if msg.text in ["Mee","mee",".mee",".Mee","คทท","/mee"]:
                    line.sendText(msg.to,"ðﾟﾘﾂห่าสูนี้กะMeทั้งคืนห่าสูðﾟﾘﾂ")
                if msg.text in ["spp","speedd",".speedd","/speedd","Spp",".Speedd"]:
                    line.sendText(msg.to,"ðﾟﾒﾫแฮงปานนี้ไปขี้ใส่นาให้แหน่ðﾟﾒﾫ")
                if msg.text in ["runtime","Runtimee","/uptimee","ออนน",".uptimre"]:
                    line.sendText(msg.to,"ðﾟﾒﾞจะเยสทำไมนานแท้ออเจ้าðﾟﾘﾋ")				
                #if msg.text in dangerMessage:
                    #random.choice(Rfu).kickoutFromGroup(receiver,[sender])
                    #random.choice(Rfu).sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)")										
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
          if settings["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = line.getGroup(op.param1)
            contact = line.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus			
            line.sendText(op.param1, " ยินดีต้อนรับ. เข้ามาแล้วก็อย่าลืมปิดแจ้งเตือนกันน่ะครับ" + line.getContact(op.param2).displayName + " สู่กลุ่ม " + "ðﾟﾑﾉ" + str(ginfo.name) + "ðﾟﾑﾈ""\nðﾟﾒﾔมาใหม่รายงานตัวด้วยจร่าðﾟﾒﾞ\nðﾟﾘﾋทำตัวดีอย่าดื้ออย่าซนละðﾟﾘﾋ")			
# ----------------- NOTIFED MEMBER OUT GROUP
        if op.type == 15:
          if settings['Lv'] == True:
            if op.param2 in bot1:
                return
            line.sendText(op.param1,"ðﾟﾒﾘGood Byðﾟﾒﾘe" + line.getContact(op.param2).displayName + "\n➰➿รีบไปไหนอ่ะ➰➿ \nðﾟﾔﾷ️ðﾟﾔﾜไม่เป็นไรไว้เจอกันใหม่นðﾟﾔﾚðﾟﾔﾷ️่ะจ๊ะ")
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\nðﾟﾔﾰ" + Name
                            pref=['eh ada','hai kak','hay kamu','nah ada','halo lg ngapain','halo','sini kak','cctv yah kak']
                            line.sendMessage(op.param1, str(random.choice(pref))+' '+Name)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print ("[ 55 ] ตรวจพบข้อความ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
