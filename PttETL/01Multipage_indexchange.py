import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
headers = {'User-Agent':userAgent}
url = 'https://www.ptt.cc/bbs/BabyMother/index{}.html'

page = 7501

for i in range(0,2):
    res = requests.get(url.format(page),headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    # print(soup)
    titleSoupList = soup.select('div[class="title"]')
    # print(titleSoupList)
    dateSoup = soup.select('div[class="date"]')
    # print(dateSoup)

    for titleSoup in titleSoupList:
        try:
            title = titleSoup.select('a')[0].text
            print(title)
            articleUrl = 'https://www.ptt.cc' + titleSoup.select('a')[0]['href']
            print(articleUrl)
        except IndexError as e:
            print(titleSoup)
    page -= 1

