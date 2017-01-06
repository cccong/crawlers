import requests
from bs4 import BeautifulSoup

import os
import re

def saveImg(url, fileName):

    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, sdch",
        'cookie': "Hm_lvt_612bedbdc93b0cf91a59fa09da7b034f=1472483825; Hm_lpvt_612bedbdc93b0cf91a59fa09da7b034f=1472485658",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.6",
        'host': "cdn.daweijita.com",
        'connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers)

    with open(fileName,'wb') as f:
        f.write(response.content)

def getSong(songUrl, songTitle, foulderTitle):
    if not os.path.exists(foulderTitle): 
        os.mkdir(foulderTitle)
    os.chdir(foulderTitle)

    songRes = requests.request("GET", songUrl)
    songSoup = BeautifulSoup(songRes.text, "html.parser")
    aLis = songSoup.find_all('a',class_=["highslide-image","downlink"])
    for i,a in enumerate(aLis):
        imgUrl = a.attrs['href']
        suffix = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', imgUrl)[0]
        fileName = songTitle + '-' + str(i+1) + suffix
        if os.path.exists(fileName): 
            print('already exist: ', fileName)
            continue
        print('get song tab number ', str(i+1), fileName)
        saveImg(imgUrl, fileName)

    os.chdir('..')

def getArtist(artistDict):
    tagName = artistDict['tagName']
    artistName = tagName[:tagName.index('<i>')]
    artistName = re.sub(r'[/\\<>:"?*|]','',artistName)
    print('get artist: ', artistName)
    
    if not os.path.exists(artistName): 
        os.mkdir(artistName)
    os.chdir(artistName)

    tagUrl = artistDict['tagUrl']
    tagRes = requests.request("GET", tagUrl)
    tagSoup = BeautifulSoup(tagRes.text, "html.parser")
    songsLis = tagSoup.find(class_='widget-content').ul.find_all('li')
    for song in songsLis:
        a = song.h2.a
        songUrl = a.attrs['href']
        songTitle = a.text
        if '【V】' in songTitle:
            print('pass', songTitle)
            continue
        foulderTitle = a.text
        try:
            songTitle = songTitle[songTitle.index('《')+1:songTitle.index('》')]
            songTitle = re.sub(r'[/\\<>:"?*|]','',songTitle)
            foulderTitle = songTitle + '-' + a.text
            foulderTitle = re.sub(r'[/\\<>:"?*|]','',foulderTitle)
        except ValueError:
            pass
        print('get song: ', songTitle)
        getSong(songUrl, songTitle, foulderTitle)
    
    os.chdir('..')


gtpFindPageUrl = "http://www.daweijita.com/tags"
gtpFindRes = requests.request("GET", gtpFindPageUrl)
gtpFindPageSoup = BeautifulSoup(gtpFindRes.text, "html.parser")
artistsScript = gtpFindPageSoup.find_all('ul',class_='all-tags')[0].next_sibling
liStr = str(artistsScript)[len('<script>var data='):-len(';</script>')]
artistsLi = eval(liStr)
for astist in artistsLi:
    print(astist)
    getArtist(astist)