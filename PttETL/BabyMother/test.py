import time
import os
import requests
import csv
from bs4 import BeautifulSoup

resource_path = r'./BabyMother'

if not os.path.exists(resource_path):
    os.mkdir(resource_path)

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

headers = {'User-Agent' : userAgent}
ss = requests.session()

url = 'https://www.ptt.cc/bbs/BabyMother/index.html'

n=1     #讀n頁

all_article_data = []

for i in range(0,n):
    res = ss.get(url, headers=headers)
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    article_title = soup.select('div[class="title"]')
    # for i in article_title:
    #     print(i)

    for each_article in article_title:
        try:
            # print(each_article.a.text)      #取出a tag的text，即標題
            # print('https://www.ptt.cc' + each_article.a['href'])    #取出atag內href的字串

            article_url = 'https://www.ptt.cc' + each_article.a['href']     #每個文章的連結
            article_text = each_article.a.text
            article_res = ss.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')
            push_up = 0
            push_down = 0
            author = ''
            title = ''
            datetime = ''
            article_content = article_soup.select('div#main-content')[0].text.split('2021')[1].split('--')[0]
            print(article_content)
        except:
            pass