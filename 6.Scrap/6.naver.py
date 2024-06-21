import requests
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/index'

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser') # 기본 파서, lxml 이라고 불리는 더 좋은 (추가 설치해야하는)

# 신문 기사제목 및 링크 출력하기
news_list = soup.select('.today_list > li')
# print(news_list)
# print(len(news_list))
for news in news_list:
    a_tag = news.select_one('a')
    # print(a_tag['title'])
    div_tag = news.select_one('.title')
    print(div_tag.text.strip())
    print(a_tag['href'])

