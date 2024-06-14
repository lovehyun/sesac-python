from flask import Flask, session, request, jsonify, send_from_directory
from flask import redirect, url_for

app = Flask(__name__)
app.secret_key = 'this-is-antoher-my-secret-hjahaha'

# 사용자 DB
users = [
    {'name': 'Alice', 'id':'alice', 'pw':'alice'},
    {'name': 'Bob', 'id':'bob', 'pw':'bob1234'},
    {'name': 'Charlie', 'id':'charlie', 'pw':'hello'},
]

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/profile')
def profile():
    return send_from_directory('static', 'profile.html')


@app.route('/api/login', methods=['POST'])
def api_login():
    # 로그인 처리를 해야함
    # id = request.form['id']  # request.form.get('id', None)
    # pw = request.form['password']

    # 데이터를 json 으로 처리해서 받아야함.
    data = request.json
    id = data.get('id')
    pw = data.get('pw')

    # 이 사용자가 목록에 있는지 검사
    # user = None
    # for u in users:
    #     if u['id'] == id and u['pw'] == pw:
    #         user = u
    user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)

    if user:
        session['user'] = user # 로그인한 사용자 정보를 세션에 저장
        return jsonify({'status': 'success', 'message': '로그인에 성공하였습니다.'})
    else:
        # return render_template('index.html', error='사용자 없음')
        return jsonify({'status': 'error', 'message': '로그인에 실패하였습니다.'})
    
# 미션1. profile 에도 GET하는데, POST 할수 있어야함...
@app.route('/api/profile', methods=['GET', 'POST'])
def api_profile():
    user = session.get('user') # 위에서 내가 저장한것 다시 찾아오기

    # 미션2. if POST 요청이 왔으면???
    # 세션에서 user정보 가져와서, 이것을 우리의 user DB에서 검색해서
    # pw를 변경한다.
    if request.method == 'POST':
        new_pw = request.form['new_password']
        
        # 나의 DB 변경
        for u in users:
            if u['id'] == user['id']:
                u['pw'] = new_pw

        # 나의 세션 변경 (해도 안해도 지금은 무방함)
        user['pw'] = new_pw
        session['user'] = user

        # 미션3. 사용자에게 성공 결과를 보내준다.
        # return render_template('profile3.html', user=user, message='비밀번호 변경에 성공하였습니다.')
        return jsonify({'status': 'success', 'message': '비밀번호 변경에 성공하였습니다.'})

    # return render_template('profile3.html', user=user)
    return jsonify({'status': 'success', 'user': user})

@app.route('/api/logout')
def api_logout():
    session.pop('user', None) # 세션에서 사용자(user) 정보 삭제
    # return redirect(url_for('home')) # 로그아웃 이후 홈 페이지로 보내주기
    return jsonify({'status':'success', 'message': '로그아웃에 성공하였습니다.'})

if __name__ == "__main__":
    app.run(debug=True)
