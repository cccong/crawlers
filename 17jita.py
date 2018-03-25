import requests
from bs4 import BeautifulSoup
import os
import re


def get_soup(url):
    res = requests.get(url)
    res.encoding = 'gbk'
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    return soup


def save_img(file_name, url):
    if not url.startswith('http'):
        url = base_url + url
    response = requests.get(url)

    with open(file_name, 'wb') as f:
        f.write(response.content)


def get_song_crawler(song_path, song_name):
    def song_crawler(song_url, img_num):
        song_soup = get_soup(song_url)
        print(song_url)
        img_url = ''
        img_name = ''
        suffix = ''
        print(song_soup.select('#article_contents img'))
        if(len(song_soup.select('#article_contents img')) > 0):
            img_url = song_soup.select('#article_contents img')[0]['src']
            suffix = img_url.split('.')[-1]
        else:
            img_url = song_soup.select('#article_content a')[0]['href']
            suffix = song_soup.select('#article_content a img')[0].string.split('.')[-1]

        img_name = os.path.join(song_path, song_name + '_' + str(img_num) + '.' + suffix)
        save_img(img_name, img_url)
        song_next_a = song_soup.find('a', class_="nxt")
        if (song_next_a):
            song_next_url = 'http://www.17jita.com/' + song_next_a['href']
            song_crawler(song_next_url, img_num+1)

    return song_crawler

base_url = 'http://www.17jita.com/'
page_url_tab = 'http://www.17jita.com/tab/img/index.php?page={}'
base_path = r'e:\jita'
flag = True


for page_num in range(44,318):
    print('------------------ '+str(page_num)+' -------------------------')
    page_url = page_url_tab.format(page_num)
    page_soup = get_soup(page_url)
    ul = page_soup.select('#ct > div.mn > div.bm > div.bm_c.xld')[0]
    for dl in ul.find_all('dl'):
        song_a = dl.find_all('a')[0]
        song_name = song_a.string.replace('/','_')
        r = re.compile(r'[\\/:*?<>|]')
        song_name = r.sub('_', song_name)
        try:
            _1, singer_name, *_2 = song_name.split(' ')
        except ValueError as v:
            singer_name = 'others'

        print(song_name)
        song_url = base_url + song_a['href']
        if song_url.split('/')[-2] != 'img': continue
        singer_path = os.path.join(base_path,singer_name)
        if not os.path.exists(singer_path):
            os.mkdir(singer_path)
        song_path = os.path.join(base_path, singer_name, song_name)
        if not os.path.exists(song_path):
            os.mkdir(song_path)
        else:
            continue
        song_crawler = get_song_crawler(song_path, song_name)
        try:
            song_crawler(song_url,1)
        except Exception as e:
            print('---------------------- error ---------------------------')
            print(song_url)
            print(e)
            print('---------------------- error ---------------------------')

# for page_num in range(1,8):
#     print('------------------ '+str(page_num)+' -------------------------')
#     page_url = page_url_tab.format(page_num)
#     page_soup = get_soup(page_url)
#     ul = page_soup.select('#ct > div.mn > div.bm > div.bm_c.xld > ul')[0]
#     for li in ul.find_all('li'):
#         a = li.find('a', class_='xi2')
#         singer_url = base_url + a['href']
#         singer_name = os.path.join(base_path, a.string)
#         print(singer_name)
#         # if ('张杰' in singer_name):
#         #     flag = False
#         #
#         # if(flag):
#         #     continue
#         if not os.path.exists(singer_name):
#             os.mkdir(singer_name)
#
#         singer_soup = get_soup(singer_url)
#         song_ul = singer_soup.select('#article_content > ul')[0]
#         for song_li in song_ul.find_all('li'):
#             song_a = song_li.find_all('a')[1]
#             song_name = song_a.string.replace('/','_').replace('\\','_')
#             print(song_name)
#             song_url = base_url + song_a['href']
#             if song_url.split('/')[-2] != 'img': continue
#             song_path = os.path.join(singer_name, song_name)
#             if not os.path.exists(song_path):
#                 os.mkdir(song_path)
#             song_crawler = get_song_crawler(song_path, song_name)
#             try:
#                 song_crawler(song_url,1)
#             except Exception as e:
#                 print('---------------------- error ---------------------------')
#                 print(song_url)
#                 print('---------------------- error ---------------------------')


