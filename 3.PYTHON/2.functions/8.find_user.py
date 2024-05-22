users = [ # 딕셔너리 리스트
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Jeju", "car": "K5"},

]

# users = ["Alice", "Bob", "Charlie"]  # 스트링 리스트

# print(users)

def find_user(name):
    # 사용자를 찾는것이 목적임!!!
    found_user = []

    for u in users:
        # print(u['name'])
        if u.get("name").lower() == name.lower(): # alice
            # print(u)
            found_user.append(u)

    return found_user

    # print('찾는 사용자가 없습니다')

found = find_user('alice')
print(f'찾은 사용자: {found}')

# find_user('alice')
# find_user('ALICE')
