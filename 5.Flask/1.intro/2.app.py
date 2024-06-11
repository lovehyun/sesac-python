from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/user/<name>')  # 기본값은 string 으로 처리함
def user(name):
    return f"<H1>Hello, {name}님!</H1>"

@app.route('/user/<int:age>')
def userage(age):
    return f"<H1>Age: {age}</H1>"

@app.route('/user/<float:weight>')
def userweight(weight):
    return f"<H1>Weight: {weight}</H1>"

@app.route('/user/<name>/<int:age>')
def usernameage(name, age):
    return f"<H1>Hello, {name}님, Age는 {age} 입니다."

@app.route('/user/<name>/<age>/<weight>')
def usernameageweight(name, age, weight):
    return f"<H1>Hello, {name}님, Age는 {age}, Weight는 {weight} 입니다."


if __name__ == "__main__":
    app.run(debug=True)
