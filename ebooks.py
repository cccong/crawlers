import requests
from bs4 import BeautifulSoup

headers = {
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
           'cache-control': 'max-age=0',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }


def get_index():
    url = 'https://www.planetebook.com/ebooks/'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text)
    pelistlinks = soup.find_all('p', class_='pelistlinks')
    print(pelistlinks[0])
    print(pelistlinks[0].a)
    print(pelistlinks[0].a['href'])
    return [p.a['href'] for p in pelistlinks]


def get_book(path):
    url = f'https://www.planetebook.com{path}'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text)
    donwload_buttons = soup.find_all('a', class_='buttonpe')
    return [a['href'] for a in donwload_buttons]


book_page_paths = get_index()
print(book_page_paths)
print('+' * 30)
for path in book_page_paths:
    book_links = get_book(path)
    for link in book_links:
        print(f'https://www.planetebook.com{link}')
