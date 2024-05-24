# https://docs.python.org/ko/3/library/datetime.html
import datetime  # 객체라서, 객체안의 멤버를 부르기 위해서

# 모듈명.클래스(객체)명.함수명 (Class/Object)

# 현재 시간 출력
current_time = datetime.datetime.now()
print(current_time)

# 내가 원하는 시간 생성
my_time = datetime.datetime(2024, 1, 1, 10, 30, 0)
print(my_time)
print(type(my_time))

my_time2 = datetime.date(2019, 12, 4)
