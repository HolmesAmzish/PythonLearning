import re
import os
from time import sleep
from urllib.parse import urljoin
from urllib.request import urlopen
from multiprocessing import Pool

dst_dir = 'new_folder'
if not os.path.isdir(dst_dir):
    os.mkdir(dst_dir)

url = r'http://www.cae.cn/cae/html/main/col48/column_48_1.html'
with urlopen(url) as response:
    content = response.read().decode()

pattern = r'<li class="name_list"><a href="(.+?)" target="_blank">(.+?)</a></li>'
result = re.findall(pattern, content)


def crawl_every_url(item):
    per_url, name = item
    per_url = urljoin(url, per_url)  # 修正了这里
    name = os.path.join(dst_dir, name)
    print(per_url)
    try:
        with urlopen(per_url) as response:
            content = response.read().decode()
    except Exception as e:
        print(f'Something went wrong: {e}, try after 1 sec...')
        sleep(1)
        crawl_every_url(item)
        return

    pattern = r'<img src="(.+?)" style=.*?/>'
    img_urls = re.findall(pattern, content)
    if img_urls:
        img_url = urljoin(url, img_urls[0])
        try:
            with urlopen(img_url) as response_1:
                with open(f'{name}.jpg', 'wb') as fp:
                    fp.write(response_1.read())  # 直接写入文件
        except Exception as e:
            print(f'Failed to download image {img_url}: {e}')

    pattern = r'<p>(.+?)</p>'
    intro = re.findall(pattern, content, re.M)
    if intro:
        intro = '\n'.join(intro)
        intro = re.sub(r'(&ensp;)|(&nbsp;)|(<a href.*?</a>)', '', intro)
        with open(f'{name}.txt', 'w', encoding='utf-8') as fp:
            fp.write(intro)


if __name__ == '__main__':
    with Pool(10) as p:
        p.map(crawl_every_url, result)