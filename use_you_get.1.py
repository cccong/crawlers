import subprocess
import os
import time

base_path = r'E:\base_path'

def download(url, name, idx):
    outf = open(f'{idx}.log', 'a', encoding='utf-8')
    path = os.path.join(base_path, 'guhanyu', str(idx))
    if not os.path.exists(path):
        os.makedirs(path)
    
    print('create task:', url)
    
    return subprocess.Popen(
        [
            'you-get',
            '-o',
            path,
            '-O',
            name,
            url,
            '--debug'
        ],
        stdout=outf,
        stderr=outf
    )
    

def create_task(idx, page):
    url = f'https://www.bilibili.com/video/av6931030/?p={page}'
    return {
        'p':download(url, page, idx),
        'page':page,
        'idx':idx
    }
    
tasks = []
page = 1
for idx in range(3):
    tasks.append(create_task(idx, str(page)))
    page += 1

while True:
    for idx,task in enumerate(tasks):
        re_code = task['p'].poll()
        print(f'process: [{idx}], code: {re_code}')
        if re_code and re_code == 0:
            tasks[idx] = create_task(idx, page)
            page += 1
        if re_code and re_code != 0:
            tasks[idx] = create_task(idx, task['page'])
    time.sleep(3)

