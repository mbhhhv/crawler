import requests
from lxml import etree
import time
import csv

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/122.0.0.0 Safari/537.36'}


def get_urls():
    urls = [f'https://book.douban.com/top250?start={num}' for num in range(0, 226, 25)]
    return urls


def get_info(url):
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    infos = html.xpath('//tr[@class="item"]')
    for info in infos:
        book_name = info.xpath('td/div/a/@title')[0]
        book_url = info.xpath('td/div/a/@href')[0]
        book_info = info.xpath('td/p/text()')[0]
        author = book_info.split('/')[0]
        publisher = book_info.split('/')[-3]
        date = book_info.split('/')[-2]
        price = book_info.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')
        comment = info.xpath('td/p/span/text()')
        writer.writerow((book_name, book_url, author, publisher, date, price, rate, comment))


if __name__ == '__main__':
    f = open('data.csv', 'w', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(('book_name', 'url', 'author', 'publisher', 'date', 'price', 'rate', 'comment'))
    urls = get_urls()
    for url in urls:
        get_info(url)
    f.close()
