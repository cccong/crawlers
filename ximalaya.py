import requests
from bs4 import BeautifulSoup

albumPage = requests.get('http://www.ximalaya.com/63448944/album/5716040')
print(albumPage.status_code)

albumPageSoup = BeautifulSoup(albumPage.text, "html.parser")

ul = albumPageSoup.find('div',class_='album_soundlist').ul.find_all('li')

for li in ul:
    sound_id = li['sound_id']
    url = 'http://www.ximalaya.com/tracks/{}.json'.format(sound_id)
    sound_res = requests.get(url).json()
    print(sound_res['play_path_64'], sound_res['title'])
    m4a = requests.get(sound_res['play_path_64'])
    with open(sound_res['title']+'.m4a', 'wb') as m4aFile:
        m4aFile.write(m4a.content)
        print('downloaded {}'.format(sound_res['title']))


