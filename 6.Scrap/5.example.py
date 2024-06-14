import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonscraping.com/pages/page3.html'

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

# 여기에서 상품명과 가격을 출력하시오
# 웹브라우저에서 F12눌러서 소스를 봐가면서... 내가 원하는 정보가 어디있는지 확인하기
# table_tag = soup.find('table', id="giftList")
# table_tag = soup.select('#giftList')[0]
table_tag = soup.select_one('#giftList')
# print(table_tag)

# product_trs = table_tag.find_all('tr')
product_trs = table_tag.select('tr')
# print(product_trs)

item_list = []

for product_tr in product_trs[1:]:
    product_tds = product_tr.select('td')
    # print(product_tds[0], product_tds[2])
    item_list.append((product_tds[0].text.strip(), product_tds[2].text.strip()))
    # print(f"상품명: {product_tds[0].text.strip()} 가격: {product_tds[2].text.strip()}")

print(item_list)

for item in item_list:
    print(f'상품명: {item[0]}, 가격: {item[1]}')

