# 1. 반복문을 이용하여 화면에 삼각형 출력하기
# row = input('출력을 원하는 높이를 입력하세요: ')
# num_rows = int(row)
# for i in range(1, num_rows + 1):
#     print('*' * i)


# row = int(input('출력을 원하는 높이를 입력하세요: '))
# for i in range(1, row):
#     print('*' * i)

# row = input('출력을 원하는 높이를 입력하세요: ')
# for i in range(1, int(row)):
#     print('*' * i)

rows = 5

for i in range(1, rows+1):
    print(rows-i, i)


for i in range(1, rows+1):
    print(' ' * (rows-i), '*' * i)

for i in range(1, rows+1):
    print(' ' * (rows-i), '*' * (2 * i - 1))
