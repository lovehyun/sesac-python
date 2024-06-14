# pip install bs4

from bs4 import BeautifulSoup

import requests

html_doc = """
<html>
<head>
   <title>간단한 HTML 예제</title>
</head>
<body>
   <div class="container">
      <h1>안녕하세요</h1>
      <p>이것은 간단한 HTML 예제입니다.</p>
   </div>
   <a href="https://www.naver.com">네이버 링크</a>
   <img src="example.jpg" alt="예제 이미지">
   <img src="example2.jpg" alt="예제 이미지2" width="500" height="600">
   <div class="content">
      <ul>
         <li>항목 1</li>
         <li>항목 2</li>
         <li>항목 3</li>
      </ul>
   </div>
   <div id="footer">
      <p>Copyright C <b>2024.</b> 이 <i>페이지는</i> 내꺼</p>
   </div>
</body>
</html>
"""
# html_doc = requests.get('https://www.naver.com').text

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, lxml

link_tag = soup.select_one('a')
print(link_tag)

all_imgs = soup.select('img')
print(all_imgs)
for img in all_imgs:
    print(img['src'])

content_div = soup.select_one('div.content')  # div 아래에 있는 .content <-- 클래스명
print(content_div)

footer_div = soup.select_one('div#footer')
print(footer_div)

li_lists = soup.select('div.content li') # div 아래있는 content 클래스 아래있는 li들...
print(li_lists)

li_lists = soup.find_all('div.content li')  # find 시리즈는 태그명 등으로 검색하는것...
print(li_lists)

p_tag_div_footer = soup.select_one('div#footer p')
b_text = p_tag_div_footer.select_one('b').text
i_text = p_tag_div_footer.select_one('i').get_text()

print(f"볼드텍스트: {b_text}, 이탤릭텍스트: {i_text}")
