import aiohttp
import asyncio
from bs4 import BeautifulSoup


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}


async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        soup = BeautifulSoup(await response.text())
        donwload_buttons = soup.find_all('a', class_='buttonpe')
        for link in (a['href'] for a in donwload_buttons):
            print(f'https://www.planetebook.com{link}')



async def download(session, url):
    file_name = url.split('/')[-1].strip('\n')
    print(f'start download {url}')
        
    async with session.get(url, headers=headers) as response:
        res = await response.read()
        f = open('E:\\Documents\\ebooks\\'+file_name, 'wb')
        f.write(res)
        print(f'download complete {file_name}')


async def main():
    jar = aiohttp.CookieJar(unsafe=True)
    conn = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(cookie_jar=jar, connector=conn) as session:
        tasks = []
        books = ['/the-adventures-of-huckleberry-finn/', '/the-adventures-of-tom-sawyer/', '/aesops-fables/', '/agnes-grey/', '/alices-adventures-in-wonderland/', '/andersens-fairy-tales/', '/anna-karenina/', '/anne-of-green-gables/', '/around-the-world-in-80-days/', '/beyond-good-and-evil/', '/bleak-house/', '/the-brothers-karamazov/', '/a-christmas-carol/', '/crime-and-punishment/', '/david-copperfield/', '/down-and-out-in-paris-and-london/', '/dracula/', '/dubliners/', '/emma/', '/erewhon/', '/for-the-term-of-his-natural-life/', '/frankenstein/', '/great-expectations/', '/the-great-gatsby/', '/grimms-fairy-tales/', '/gullivers-travels/', '/heart-of-darkness/', '/the-hound-of-the-baskervilles/', '/the-idiot/', '/the-iliad/', '/the-island-of-doctor-moreau/', '/jane-eyre/', '/the-jungle-book/', '/kidnapped/', '/lady-chatterlys-lover/', '/the-last-of-the-mohicans/', '/the-legend-of-sleepy-hollow/', '/les-miserables/', '/little-women/', '/madame-bovary/',
                 '/the-merry-adventures-of-robin-hood/', '/the-metamorphosis/', '/middlemarch/', '/moby-dick/', '/1984/', '/northanger-abbey/', '/nostromo-a-tale-of-the-seaboard/', '/notes-from-the-underground/', '/the-odyssey/', '/of-human-bondage/', '/oliver-twist/', '/paradise-lost/', '/persuasion/', '/the-picture-of-dorian-gray/', '/pollyanna/', '/the-portrait-of-a-lady/', '/a-portrait-of-the-artist-as-a-young-man/', '/pride-and-prejudice/', '/the-prince/', '/robinson-crusoe/', '/the-scarlet-pimpernel/', '/sense-and-sensibility/', '/sons-and-lovers/', '/the-strange-case-of-dr-jekyll/', '/swanns-way/', '/a-tale-of-two-cities/', '/the-tales-of-mother-goose/', '/tarzan-of-the-apes/', '/tender-is-the-night/', '/tess-of-the-durbervilles/', '/the-thirty-nine-steps/', '/the-three-musketeers/', '/the-time-machine/', '/treasure-island/', '/the-trial/', '/ulysses/', '/utopia/', '/vanity-fair/', '/war-and-peace/', '/within-a-budding-grove/', '/women-in-love/', '/wuthering-heights/']
        books = open('book_url.txt')
        for book in books:
            if '.mobi' in book:
                continue
            tasks.append(asyncio.ensure_future(
                download(session, book.strip('\n'))))
        await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
