import requests
from lxml import etree
import time
import csv

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/122.0.0.0 Safari/537.36'}


def get_urls():
    urls = [f'https://www.qidian.com/all/page{num}/' for num in range(1, 6)]
    return urls


def get_info(url):
    res = requests.get(url, headers=headers)
    print((res.text))
    html = etree.HTML(res.text)
    infos = html.xpath('//ul[@class="all-img-list cf"]/li')
    print(infos)
    for info in infos:
        book_name = info.xpath('div[2]/h2/a/text()')[0]
        print(book_name)
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        style1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        style = style1 + '.' + style2
        complete = info.xpath('div[2]/p[1]/span/text()')[0]
        introduce = info.xpath('div[2]/p[2]/text()')[0]
        word_num = info.xpath('div[2]/p[3]/span/span/text()')[0]
        # print((book_name, author, style, complete, introduce, word_num))
        writer.writerow((book_name, author, style, complete, introduce, word_num))


if __name__ == '__main__':
    f = open('xiaoshuo.csv', 'w',encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(('book_name', 'author', 'style', 'complete', 'introduce', 'word_num'))
    urls = get_urls()
    for url in urls:
        get_info(url)
        time.sleep(1)
    f.close()
