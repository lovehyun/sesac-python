from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-1234'},
    {'name': 'Alice', 'age': 30, 'phone': '123-321-4321'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-2345'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-5555'},
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/search')
def search():
    name_query = request.args.get('name')
    age_query = request.args.get('age')
    result = users

    # 미션1. 위에 있는 users 에서 query 구문이 name 인 사람을 찾아서 출력하시오..
    # for u in users:
    #     if u['name'].lower() == name_query.lower():
    #         users = u

    if name_query:
        result = [u for u in users if name_query.lower() in u['name'].lower()]

    # 미션2. 나이도 검색... age
    if age_query:
        try:
            age_query = int(age_query)
            result = [u for u in result if age_query == u['age']]
        except ValueError:
            # return jsonify({'error':'Age parameter must be an 숫자'}), 400
            return json.dumps({'error': '나이는 숫자로 입력해야 합니다.'}, ensure_ascii=False), 400

    print(result)

    # 미션3. 전화번호 끝 4자리로 검색... phone

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
