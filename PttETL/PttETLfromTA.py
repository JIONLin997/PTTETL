import time
import os
import requests
from bs4 import BeautifulSoup

resource_path = r'./BabyMother'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

headers = {'User-Agent' : userAgent}
ss = requests.session()

url = 'https://www.ptt.cc/bbs/BabyMother/index.html'

try:
    print(each_article.a.text)  # 取出a tag的text
    print('https://www.ptt.cc' + each_article.a['href'])  # 取出atag內href的字串

    article_url = 'https://www.ptt.cc' + each_article.a['href']
    article_text = each_article.a.text
    article_res = ss.get(article_url, headers=headers)
    article_soup = BeautifulSoup(article_res.text, 'html.parser')














