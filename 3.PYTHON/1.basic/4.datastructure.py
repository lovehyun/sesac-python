# 자료 구조 배우는 중....
# 1. 리스트
a = 5
a2 = [5]
b = [10, 20, 30, 40, 50]

print(a)
print(a2)
print(b)

print(b[0])
print(b[4])
# print(b[5]) # IndexError발생

print(len(b)) # 길이는 우리가 일반적으로 사용하는 그 길이
            # 인덱스는 0 ~ 길이-1

print(b[1:3])

fruits = ['apple', '사과', 'grape', '포도']
print(fruits)

print(fruits[1:3])

members = [3, '"my" desk and chair', 2, -1, "chair"]
print(members)

b.remove(20)
print(b)

fruits.remove('apple')
print(fruits)

# insert 삽입, append 덧붙이기...
b.append(20)
print(b)

b.insert(0, 20)
print(b)

# a.insert(0, 10) # TypeError
a2.insert(0, 10)
print(a2)

# --------------------------------
# 2. 튜플 (tuple) - 리스트와 동일한데, 변경 불가한 리스트를 생성 - 이뮤터블(Immutable)

c = (1,2,3,4,5)
print(c)

# c.remove(2) # 삭제 불가
# c.append(2) # 삽입 불가

print(c[3], c[4])
print(c[2:])
print(b[2:])
print(c[:2])
print(b[:2])

# -------------------------------
# 3. 딕셔너리 (dict, dictionary) 라는 데이터 타입 - Key, value

user1 = {
    "name":"park",
    "age":10,
    "city":"seoul"
}

print(user1)
print(user1['name'])
print(user1['age'])
print(user1['city'])
# print(user1['email'])   # KeyError 발생... 없는 키 참조

user1['email'] = 'hello@email.com'
print(user1)

user1['email'] = ''
print(user1)

del user1['email']
print(user1)
