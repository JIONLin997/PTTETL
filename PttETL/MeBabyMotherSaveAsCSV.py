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

n = 1   # 讀n頁

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
            print(each_article.a.text)      #取出a tag的text，即標題
            print('https://www.ptt.cc' + each_article.a['href'])    #取出atag內href的字串

            article_url = 'https://www.ptt.cc' + each_article.a['href']     #每個文章的連結
            article_text = each_article.a.text
            article_res = ss.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')
            push_up = 0
            push_down = 0
            author = ''
            title = ''
            datetime = ''
            try:
                article_content = article_soup.select('div#main-content')[0].text.split('--')[0]   #以時間作為split，也可以當作時間基準(即爬2021年的文章)，否則定位不到文章內容，幹
            except:
                pass
            push_list = article_soup.select('div[class="push"] span')
            # for i in push_list:
            #     print(i)
            for number in push_list:
                if '推' in number.text:
                    push_up += 1
                if '噓' in number.text:
                    push_down += 1
            article_info_list = article_soup.select('span[class="article-meta-value"]')
            # for i in article_info_list:   #觀察上面list的形式 : [0]=作者 [1]=看板名稱 [2]=文章標題 [3]=文章時間
            #     print(i)
            try:
                author = article_info_list[0].text
                title = article_info_list[2].text
                datetime = article_info_list[3].text
                #print(author)
            except:
                pass
            all_article_message = article_soup.select('span[class="f3 push-content"]')         #一篇文章下的所有留言
            for each_message in all_article_message:
                try:
                    article_message = each_message.text.split(": ")[1]
                    article_data = {'文章標題': title, '文章網址': article_url, '文章作者': author, '留言': article_message,
                                    '文章內容': article_content}
                    all_article_data.append(article_data)
                except:
                    pass

        except AttributeError as e:
            print('==========')
            print(each_article)
            print(e.args)
            print('==========')
    url = 'https://www.ptt.cc' + soup.select('div[class="btn-group btn-group-paging"]')[0].select('a')[1]['href'] # [1]是上一頁

fn = 'PttBabyMother5.csv'
columns_name = ['文章標題', '文章網址', '文章作者', '留言', '文章內容']
with open(fn, 'w', newline='', encoding='utf-8') as csvFile:
    dictWriter = csv.DictWriter(csvFile, fieldnames=columns_name)
    dictWriter.writeheader()
    for data in all_article_data:
        dictWriter.writerow(data)




