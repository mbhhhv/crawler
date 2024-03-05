import requests
from bs4 import BeautifulSoup
import time

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

'''
def get_links(url):
    response = requests.get(url, headers)
    soup = BeautifulSoup('response.text', 'lxml')
    links = soup.select('#content_left')
    for link in links:
        href = link.get('href')
        get_info(href)


def get_info(url):
    response = requests.get(url, headers)
    soup = BeautifulSoup('response.text', 'lxml')
    texts = soup.find_all('p')
    for text in texts:
        print(text.text)
'''

if __name__ == '__main__':
    keyword = '电信网络诈骗'  # keyword是电信网络诈骗
    urls = {
        (f'https://www.baidu.com/s?wd={keyword}&base_query={keyword}&pn={number}'
         f'&oq={keyword}&tn=15007414_20_dg&ie=utf-8&usm=3')
        for number in range(0, 50, 10)}

    for url in urls:
        print(url)
        response = requests.get(url, headers)
        soup = BeautifulSoup('response.text', 'lxml')
        links = soup.find_all('div')
        print(links)

        '''
        for link in links:
            href = link.get('href')
            print(href)
        time.sleep(2)
'''
