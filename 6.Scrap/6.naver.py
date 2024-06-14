import requests
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/index'

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

# 신문 기사제목 및 링크 출력하기
news_list = soup.select('.today_list > li')
# print(len(news_list))
for news in news_list:
    a_tag = news.select_one('a')
    print(a_tag['title'])
    print(a_tag['href'])