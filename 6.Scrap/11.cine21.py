import requests
from bs4 import BeautifulSoup

# 웹 페이지에 GET 요청 보내기
url = 'http://www.cine21.com/rank/boxoffice/domestic'
response = requests.get(url)

# 응답의 텍스트를 BeautifulSoup으로 파싱
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

# boxoffice_list_content = soup.find('div', id='boxoffice_list_content')
boxoffice_list_content = soup.select_one('#boxoffice_list_content')
# print(boxoffice_list_content)
