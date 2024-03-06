import re
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 '
                  'Safari/537.36'}
url = 'https://book.qidian.com/info/1209977/?source=m_jump#Catalog'

def get_herfs(url):
    res = requests.get(url, headers=headers)
    # soup = BeautifulSoup(res.text,'lxml')
    herfs = re.findall('<a href="//(.*?)" target="_blank" data-eid="qd_G55"', res.text, re.S)
    chapters = re.findall(' alt="斗破苍穹 (.*?)在线阅读" title="斗破苍穹', res.text, re.S)

    chapter_url = {}
    f1 = open('chapter_url.txt', 'w')
    f2 = open('url.txt', 'w')
    for chapter, herf in zip(chapters, herfs):
        chapter_url = {
            'chapter': chapter.strip(),
            'url': herf.strip()
        }
        lines1 = [chapter.strip()      ,herf.strip(),'\n']
        lines2 = [herf.strip(),'\n']
        f1.writelines(lines1)
        f2.writelines(lines2)
    f1.close()
    f2.close()



if __name__ == '__main__':
    get_herfs(url)

