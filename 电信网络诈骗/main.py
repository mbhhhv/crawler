import requests
from bs4 import BeautifulSoup

url = 'https://baike.baidu.com/item/%E7%94%B5%E4%BF%A1%E8%AF%88%E9%AA%97/6590062?fr=ge_ala'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}


def get_info(url):
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.text, 'lxml')
    texts = soup.find_all('span')
    return texts


def in_file(texts):
    f = open('data.txt', 'w')
    for text in texts:
        f.write(text.text)
    f.close()


if __name__ == '__main__':
    texts=get_info(url)
    in_file(texts)
