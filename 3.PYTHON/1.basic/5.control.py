count = 0

print('while')
while (count <= 10):  # 이 조건이 True인 동안
    print(count)
    count = count + 2

print('for')
for i in range(5): # range(5) = [0,1,2,3,4]
    print(i)

users = ['park', 'kim', 'lee', 'son']
for name in users:
    print(name)

for num in [-5, 7, 133, 'park', 'sesac']:
    print(num)

for i in range(3,7): # range(3,7) = [3,4,5,6]
    print(i)

for i in range(1,10,2): # range(1,10,2) = [1,3,5,7,9]
    print(i)

