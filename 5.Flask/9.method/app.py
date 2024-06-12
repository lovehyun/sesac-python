from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'id':'alice', 'pw':'alice'},
    {'name': 'Bob', 'id':'bob', 'pw':'bob1234'},
    {'name': 'Charlie', 'id':'charlie', 'pw':'hello'},
]

@app.route('/', methods=['GET', 'POST'])
def home():
    # id = request.args.get('id') # 이거는 GET방식의 URL 파리미터를 처리할때만 가능...

    if request.method == 'POST':
        id = request.form['id'] # 여기는 POST방식 중에서, FORM-Data를 처리할때 Payload를 받아오는 방법
        pw = request.form['password']

        # user = None
        # for u in users:
        #     if u['id'] == id and u['pw'] == pw:
        #         print('매치되는 사용자가 있음!!!')
        #         user = u

        # 위 5줄짜리 코드를 1줄로, next() 함수와 list comprehension 으로 작성하기
        # next() 함수는, next(iterate조건문, 기본값) 형태로 구성됨
        user = next((user for user in users if user['id'] == id and user['pw'] == pw), None)

        # 위에 있는 user 목록과 입력한 id/pw 를 비교해서, print로 로그인 허용/불허 출력
        print(f'입력한ID: {id}, 입력한PW: {pw}')
        
        if user:
            print(f"로그인한 사용자는 {user['name']} 입니다.")
            # return f'<H1>로그인 성공!!</H1>'
            # return render_template('success.html', user=user)
            message = None
        else:
            print(f'로그인 가능한 사용자가 없습니다. id={id}')
            message = '로그인 실패'
            # return f'<H1>로그인 실패!!</H1>'
            # return render_template('failure.html', user=user)
        
        return render_template('index.html', user=user, error=message) 


    # 위 내용을 아래 HTML에 전달하시오....
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(debug=True)
