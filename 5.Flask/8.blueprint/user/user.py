from flask import Blueprint, render_template

user_app = Blueprint('user', __name__)

@user_app.route("/") # 여기서의 / 는 blueprint 를 등록한 app 에서 정의한 prefix 가 기본값
def home():
    return render_template('user/index.html')
