from flask import Flask, render_template, request

app = Flask(__name__)

# users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-456-7890'},
    {'name': 'Alice', 'age': 30, 'phone': '123-456-7890'},
    {'name': 'Bob', 'age': 30, 'phone': '987-654-3210'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-123-4567'}
]

@app.route('/')
def main():
    return render_template("index.html", users=users)

@app.route('/user')
def get_user_by_name():
    search_name = request.args.get('name')
    search_age = request.args.get('age')
    print(f"검색한이름:{search_name}, 검색한나이:{search_age}")

    filtered_user = users

    if search_name:
        filtered_user = [u for u in filtered_user if search_name.lower() in u['name'].lower()]

    if search_age:
        filtered_user = [u for u in filtered_user if int(search_age) == u['age']]

    return render_template('index.html', users=filtered_user)

if __name__ == "__main__":
    app.run(debug=True)

