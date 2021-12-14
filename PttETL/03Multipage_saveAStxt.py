import requests
import os
from bs4 import BeautifulSoup
import time

if not os.path.exists('./pttBabyMother'):
    os.mkdir('./pttBabyMother')

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
headers = {
    'User-Agent':userAgent
}
url = 'https://www.ptt.cc/bbs/BabyMother/index.html'

for i in range(0,2):
    res = requests.get(url,headers=headers)

    soup = BeautifulSoup(res.text,'html.parser')
    # print(soup)

    titleSoupList = soup.select('div[class="title"]')
    print(titleSoupList)

    for titleSoup in titleSoupList:
        try:
            time.sleep(random.randint(1,50)/10)     # 防短時間存取太多次
            title = titleSoup.select('a')[0].text
            articleUrl = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
            # Get article content
            resArticle = requests.get(articleUrl, headers=headers)
            soupArticle = BeautifulSoup(resArticle.text, 'html.parser')
            articleContent = soupArticle.select('div[id="main-content"]')[0].text.split('※ 發信站')[0]
            try:
                with open('./pttBabyMother/{}.txt'.format(title),'w', encoding='utf-8') as f:
                    f.write(articleContent)
            except FileNotFoundError:   # 文章有'/'導致程序認為是路徑
                with open('./pttBabyMother/{}.txt'.format(title.replace('/','')),'w', encoding='utf-8') as f:
                    f.write(articleContent)
            except OSError:     # windows有額外非法字元
                pass
            print(title)
            print(articleUrl)
        except IndexError as e:
            print(e)
        except:
            pass
        print("=====")
    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]['href']
    #print(url)
