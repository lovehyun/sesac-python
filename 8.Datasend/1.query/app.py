from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/user_json', methods=["GET", "POST", "DELETE"])
def json_parse():
    data = request.json
    print(data)
    return data

@app.route('/user', methods=["GET"])
def query_params():
    name = request.args.get('name')  # 이거 있나??
    age = request.args.get('age', 0) 
    # name = request.args['name']  # 무조건 달라고 때쓰는것..
    # age = request.args['age']
    return f"Name: {name}, Age: {age}"

@app.route('/user', methods=["POST"])
def form_params():
    # name = request.form.get('name')  # 이거 있나??
    # age = request.form.get('age', 0) 
    name = request.form['name']  # 무조건 달라고 때쓰는것..
    age = request.form['age']
    return f"Name: {name}, Age: {age}"

if __name__ == "__main__":
    app.run(debug=True)
