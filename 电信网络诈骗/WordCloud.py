import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt



f = open('data.txt','r')
text = f.read()

text = ((text.replace('等','').replace('的','').replace('在','')
        .replace('年','')).replace('月',';').replace('了','')
        .replace('和',''))

# 使用jieba进行中文分词
wordlist = jieba.cut(text, cut_all=False)
wl = " ".join(wordlist)

# 设置词云图的参数
wc = WordCloud(
    font_path='simhei.ttf',  # 设置字体路径，确保支持中文
    background_color="white",  # 背景颜色
    max_words=200,  # 显示最大词数
    width=1920,  # 图片宽度
    height=1080,  # 图片高度
    margin=5,  # 边缘空白处
).generate(wl)

# 使用matplotlib展示词云图
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

wc.to_file("wordcloud.jpg")