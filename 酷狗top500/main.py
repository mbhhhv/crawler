from bs4 import BeautifulSoup
import requests
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 '
                  'Safari/537.36'}

# 构造URL列表存储URL
urls = [f'https://www.kugou.com/yy/rank/home/{number}-8888.html' for number in range(1, 24)]

f = open('data.txt', 'w',encoding="utf-8")
# 构造爬取函数
def get_info(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    # 得到排名列表
    ranks = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
    # 得到歌名及歌手名列表
    all_names = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    singer_names = []
    names = []
    for all_name in all_names:
        name, singer_name = all_name.text.split('-',1)
        names.append(name)
        singer_names.append(singer_name)
    # 得到时长列表
    durations = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')

    for rank, name, singer_name, duration in zip(ranks, names, singer_names, durations):
        music = {
            'rank': rank.get_text().strip(),
            'name': name.strip(),
            'singer_name': singer_name.strip(),
            'duration': duration.get_text().strip()
        }
        print(music)
        lines = [rank.get_text().strip(),'     ',name.strip(),'     ',singer_name.strip(),'     ',duration.get_text().strip(),'\n']
        print(lines)

        f.writelines(lines)


if __name__ == '__main__':
    for url in urls:
        get_info(url)
        time.sleep(2)
    f.close()
