import math # 함수는 바로 사용 가능

# 모듈명.함수명(Function)
# 모듈명.상수명(Constant)

# 상수와 함수는 바로 호출이 가능함

print(math.pi)
print(math.pow(5, 2))  # 5의 2승 = 25

# 원의 넓이 : pi * r ^ 2 (^ = 컴퓨터에서 제곱을 표현함) 
radius = 5
area = math.pi * math.pow(radius, 2)
print(f'반지름이 {radius} 인 원의 넓이는 {area} 입니다.')

# 로그 계산
x = 2.718
log_value = math.log(x)
print("natural log: ", log_value)
