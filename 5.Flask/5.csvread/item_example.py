my_dict = {'name':'Alice', 'age':25, 'phone':'123-456-7890'}

# built-in 함수 = 내장함수 = 파이썬에 기본 탑재된...
items = my_dict.items()
items_list = list(items) # type casting = 형(type) 변환시켜주는 과정...
# print(items_list[1])  

for item in items_list:
    print(item)

for key, value in items_list:
    print(f'키: {key}, 값: {value}')  # meaningful 하게... 하는것이 좋음

print('-'* 50)

for key, value in sorted(my_dict.items()):
    print(f'키: {key}, 값: {value}')

update_dict = {'car': 'K5', 'city': 'Seoul'}

# for key, value in update_dict.items():
    # my_dict[key] = value

print(f'원본: {my_dict}')
print(f'업데이트: {update_dict}')

new_dict = my_dict | update_dict  # python 3.9 이상~
print(f'통합본: {new_dict}')

print('-'* 50)

users = [
    {'name':'Alice', 'age':25, 'phone':'123-111-7890'},
    {'name':'Bob', 'age':19, 'phone':'123-222-7890'},
    {'name':'NewBob', 'phone':'123-222-7890'},
    {'name':'Charlie', 'age':22, 'phone':'123-333-7890'},
]

filtered_user = []
for user in users:
    if user.get('age', 0) >= 20:
        filtered_user.append(user)

print(filtered_user)

filtered_user = [user for user in users if user.get('age', 0) >= 20]
print(filtered_user)

filtered_user_ages = [{key: value for key, value in u.items() if key == 'age' and value >= 20} for u in users]
print(filtered_user_ages)