users = [ # 딕셔너리 리스트
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Jeju", "car": "K5"},
    {"name": "Dave", "age": 35, "location": "Jeju", "car": "K5"},
    {"name": "June", "age": 35, "location": "Jeju", "car": "K5"},

]

def display_user(users):
    print("--- 찾은 사용자 목록 ---")
    if len(users) == 0:
        print('사용자 없음')
    else:
        for u in users:
            print(f"이름: {u['name']}, 나이: {u['age']}, 사는곳: {u['location']}")

def find_user(name=None, age=None):  # 함수의 입력
    found_user = []

    # 아무것도 없는 케이스
    # if name is None and age is None:
    if name == None and age == None:
        return users

    for u in users:
        # 둘다 입력값이 있음
        # if name is not None and age is not None:
        if name != None and age != None:
            if u["name"].lower() == name.lower() and \
               u["age"] == age:
                found_user.append(u)
        
        # 아니면, 이름만 있음
        # elif name is not None:
        elif name != None:
            if u["name"].lower() == name.lower():
                found_user.append(u)

        # 아니면, 나이만 있음
        # elif age is not None:
        elif age != None:
            if u["age"] == age:
                found_user.append(u)

    return found_user # 함수의 출력

    # print('찾는 사용자가 없습니다')

# found = find_user('alice', 25)
# found = find_user('alice')
# found = find_user(age=35) # ???? 이렇게 검색은 어떻게???
# found = find_user() # ??? 모든거 다 검색은 어떻게???

# print(f'찾은 사용자: {found}')
# display_user(found)


# 미션2. 입력인자를 하나만 받아서 검색하시오.
#  미션1에서 name 과 age로 구현을 했을때, 그 이후에 location 과 car가 추가가 계속 계속 될 수 있는데,
#  이렇게 입력 받으면 입력값이 길어지고, 함수 내용이 계속 복잡해지니, 입력 인자 하나를 받아서 구현하시오

def find_user2(search): # 딕셔너리로 받았음..
    result = []

    for u in users:
        # 조건문 적절하게 넣기... 해당 멤버가 없으면?? 그 필드 True
        if (search.get('age') is None or u.get('age') == search.get('age')) and \
           (search.get('min_age') is None or u.get('age') >= search.get('min_age')) and \
           (search.get('name') is None or u.get('name') == search.get('name')) and \
           (search.get('location') is None or u.get('location') == search.get('location')) and \
           (search.get('car') is None or u.get('car') == search.get('car')):

            result.append(u)

    return result

search_criteria1 = {"name": "Bob"}
search_criteria2 = {"name": "Alice", "age": 40}
# search_criteria2 = {"name": "Alice"}
search_criteria3 = {"location":"Jeju", "car":"BMW"}
search_criteria4 = {"location":"Jeju", "car":"K5"}
search_criteria5 = {"name": "Alice", "min_age": 20} # 기대치는 2명
search_criteria6 = {"name": "Alice", "min_age": 30} # 기대치는 1명
search_criteria7 = {"name": "Alice", "min_age": 50} # 기대치는 0명

# print(find_user2(search_criteria7))

def find_user3(search):
    result = []

    for u in users:
        if match_criteria(u, search):
            result.append(u)

    return result

# 이 user라는 사용자가 이 조건(criteria)에 만족하느냐??
# 그래서, 조건에 만족하면 True 반환, 만족하지 않으면 False 를 반납.
def match_criteria(user, criteria):  
    for key, value in criteria.items(): # 딕셔너리 안에 있는 k,v 쌍을 하나씩 추출하는 함수 = items() 함수의 기능임
        if key == "age":
            # 나이에 대해 비교
            if user["age"] != value:
                return False
        if key == "name":
           if user["name"] != value:
                return False
        if key == "location":
            if user["location"] != value:
                return False
        if key == "car":
            if user["car"] != value:
                return False
            
    return True

print(find_user3(search_criteria4))
