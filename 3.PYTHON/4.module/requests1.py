# pip install requests
import requests

# 리퀘스트 모듈안에 있는 함수를 사용할 수 있음

# 1. 웹 페이지에 있는 컨테츠 가져울수 있음
# response = requests.get("https://www.example.com")
response = requests.get("https://jsonplaceholder.typicode.com/users")
print("웹 페이지 내용: ")
print(response)
print(response.status_code)
# print(response.text)

# text 결과물 받아온것을 json 이라는 데이터타입으로 변환
data = response.json()
# print("JSON 데이터: ", data)

users = data
for user in users:
    print("이름: {}, ID: {}, 이메일: {}".format(user['name'], user['username'], user['email']))
