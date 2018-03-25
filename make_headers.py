raw_headers = ''':authority: www.planetebook.com
:method: GET
:path: /ebooks/
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7
cache-control: max-age=0
cookie: _ga=GA1.2.15391762.1521984482; _gid=GA1.2.1555915216.1521984488
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'''

headers = {}

for line in raw_headers.split('\n'):
    key, value = line.split(': ')
    headers[key] = value

print(headers)

books = ['/the-adventures-of-huckleberry-finn/', '/the-adventures-of-tom-sawyer/', '/aesops-fables/', '/agnes-grey/', '/alices-adventures-in-wonderland/', '/andersens-fairy-tales/', '/anna-karenina/', '/anne-of-green-gables/', '/around-the-world-in-80-days/', '/beyond-good-and-evil/', '/bleak-house/', '/the-brothers-karamazov/', '/a-christmas-carol/', '/crime-and-punishment/', '/david-copperfield/', '/down-and-out-in-paris-and-london/', '/dracula/', '/dubliners/', '/emma/', '/erewhon/', '/for-the-term-of-his-natural-life/', '/frankenstein/', '/great-expectations/', '/the-great-gatsby/', '/grimms-fairy-tales/', '/gullivers-travels/', '/heart-of-darkness/', '/the-hound-of-the-baskervilles/', '/the-idiot/', '/the-iliad/', '/the-island-of-doctor-moreau/', '/jane-eyre/', '/the-jungle-book/', '/kidnapped/', '/lady-chatterlys-lover/', '/the-last-of-the-mohicans/', '/the-legend-of-sleepy-hollow/', '/les-miserables/', '/little-women/', '/madame-bovary/','/the-merry-adventures-of-robin-hood/', '/the-metamorphosis/', '/middlemarch/', '/moby-dick/', '/1984/', '/northanger-abbey/', '/nostromo-a-tale-of-the-seaboard/', '/notes-from-the-underground/', '/the-odyssey/', '/of-human-bondage/', '/oliver-twist/', '/paradise-lost/', '/persuasion/', '/the-picture-of-dorian-gray/', '/pollyanna/', '/the-portrait-of-a-lady/', '/a-portrait-of-the-artist-as-a-young-man/', '/pride-and-prejudice/', '/the-prince/', '/robinson-crusoe/', '/the-scarlet-pimpernel/', '/sense-and-sensibility/', '/sons-and-lovers/', '/the-strange-case-of-dr-jekyll/', '/swanns-way/', '/a-tale-of-two-cities/', '/the-tales-of-mother-goose/', '/tarzan-of-the-apes/', '/tender-is-the-night/', '/tess-of-the-durbervilles/', '/the-thirty-nine-steps/', '/the-three-musketeers/', '/the-time-machine/', '/treasure-island/', '/the-trial/', '/ulysses/', '/utopia/', '/vanity-fair/', '/war-and-peace/', '/within-a-budding-grove/', '/women-in-love/', '/wuthering-heights/']
       
print(len(books))