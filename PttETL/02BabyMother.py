import time
import os
import requests
from bs4 import BeautifulSoup

resource_path = r'./BabyMother'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
ss = requests.session()
ss.cookies['over18'] = '1'

url = 'https://www.ptt.cc/bbs/BabyMother/index.html'

n = 2
for i in range(0,n):
    res = ss.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    article_title_html = soup.select('div[class="title"]')

    for each_article in article_title_html:
        try:
            print(each_article.a.text)
            print('https://www.ptt.cc' + each_article.a['href'])

            article_url = 'https://www.ptt.cc' + each_article.a['href']
            article_text = each_article.a.text
            article_res = ss.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')
            #print(article_res.text)

            push_up = 0
            push_down = 0
            # score = 0
            author = ''
            title = ''
            datetime = ''
            article_content = article_soup.select('div#main-content')[0].text.split('--')[0]
            article_info_list = article_soup.select('div[class="article-metaline"] span')
            for n, info in enumerate(article_info_list):
                if (n+1)%6 == 2:
                    author = info.text
                if (n+1)%6 == 4:
                    title = info.text
                if (n+1)%6 == 0:
                    datetime = info.text
            push_info_list = article_soup.select('div[class="push"] span')
            for info in push_info_list:
                if '推' in info.text:
                    push_up += 1
                if '噓' in info.text:
                    push_down += 1

            comment_info_list = article_soup.select('span[class="f3 push-content"]')
            article_content += '\n---split---\n'
            article_content += '文章作者: %s\n' % (author)
            article_content += '文章網址: %s\n' % (article_url)
            article_content += '文章標題: %s\n' % (title)
            article_content += '文章留言: '
            for i in comment_info_list:
                try:
                    comment = i.text.split(': ')[1]
                    # print(comment)
                except IndexError as e:
                    print(e.args)
                article_content += '%s' % (comment)
            article_content += '\n'
            article_content += '推: %s\n' % (push_up)
            article_content += '噓: %s\n' % (push_down)
            article_content += '時間: %s\n' % (datetime)
            try:
                with open(r'%s/%s.txt' % (resource_path, article_text), 'w', encoding='utf-8') as w:
                    w.write(article_content)
                print()
            except FileNotFoundError as e:
                print('==========')
                print(article_url)
                print(e.args)
                print('==========')
            except OSError as e:
                print('==========')
                print(article_url)
                print(e.args)
                print('==========')

        except AttributeError as e:
            print('==========')
            print(each_article)
            print(e.args)
            print('==========')

    url = 'https://www.ptt.cc' + soup.select('div[class="btn-group btn-group-paging"]')[0].select('a')[1]['href']


