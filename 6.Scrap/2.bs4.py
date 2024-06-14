# pip install bs4

from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
   <title>간단한 HTML 예제</title>
</head>
<body>
   <h1>안녕하세요</h1>
   <p>이것은 간단한 HTML 예제입니다.</p>
   <p>이것은 간단한 HTML222 예제입니다.</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, lxml
# print(html_doc)
# print(soup)
# print(html_doc.head)
# print(soup.head)
# print(soup.body.h1.text)
print(soup.p.text)