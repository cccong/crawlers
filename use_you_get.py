import subprocess
import os
import time

base_path = r'E:\base_path'

def download(url, name, idx):
    outf = open(f'{idx}.log', 'w', encoding='utf-8')
    print(url)
    path = os.path.join(base_path, 'guhanyu')
    p = subprocess.Popen(
        [
            'you-get',
            '-o',
            path,
            '-O',
            name,
            url,
        ],
        stdout=outf,
        stderr=outf
    )
    return p
    


def worker(idx, q):
    pass


url1 = 'https://www.bilibili.com/video/av6931030/?p=1'
url2 = 'https://www.bilibili.com/video/av6931030/?p=2'
tasks = [download(url1, '1.flv', 1),
download(url2, '2.flv', 2)]

while True:
    for idx,p in enumerate(tasks):
        re_code = p.poll()
        print(f'process: [{idx}], code: {re_code}')
        if re_code:
            tasks.remove(idx)
    time.sleep(2)

