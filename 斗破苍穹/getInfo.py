import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 '
                  'Safari/537.36'}


def get_info(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    info_cs = soup.find_all('script')
    for info_c in info_cs:
        print(info_c.text.strip())




if __name__ == '__main__':
    url = 'https://www.qidian.com/chapter/1209977/23194165/'
    get_info(url)

    '''
    f = open('url.txt','r')
    for url in f.readlines():
        url = 'https://' + url.strip('\n')
        get_info(url)
        '''