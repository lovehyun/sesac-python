# 파일 입출력을 할때 사용하는 함수.. open

# 파일 
# Character	Meaning
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	create a new file and open it for writing
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode

# file = open('example.txt', 'w')
# with open('example.txt', 'a') as file:
#     file.write("Hello, World2\n")

# print('텍스트 파일 기록을 완료하였습니다.')
# with open('example.txt', 'r') as file:
#     context = file.read()
#     print(context)
    
# with open('example.txt', 'r') as file:  # 파일에 접근하기위한 포인터(파일 디스크립터)
#     for line in file:
#         print(line, end='')

with open('example.txt', 'r') as file:  # 파일에 접근하기위한 포인터(파일 디스크립터)
    lines = file.readlines()
    for line in lines:
        print(line, end='')

