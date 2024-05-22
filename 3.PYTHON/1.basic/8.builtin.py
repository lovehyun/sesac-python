# while True:   # 조건문이 '참'인동안 실행한다.
#     a = input('숫자를 입력하세요: ')
#     print(a)

# 미션3. 숫자를 두개 입력 받아서, 덧셈 결과를 출력하시오.
str_a = input('첫번째 숫자를 입력하세요: ')
str_b = input('두번째 숫자를 입력하세요: ')

# input 값의 모든것은 다 문자열로 처리된다...
# 우리가 해야할것은? 형 변환... type 형...
# type casting = 타입을 변경해준다

int_a = int(str_a)
int_b = int(str_b)

print(f'두 숫자의 합은 {int_a + int_b} 입니다')
