from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# flask-sqlalchemy 설정 끝
db = SQLAlchemy(app)

# 모델 불러오기
# from models import User
# DB 모델 정의

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = request.form.get('age')

    new_user = User(name=name, age=int(age))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)
