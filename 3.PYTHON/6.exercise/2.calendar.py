import calendar

# print(calendar.month(2024, 5))

# year = int(input("연도를 입력하세요: "))
# month = int(input("월을 입력하세요: "))

# print(calendar.month(year, month))

def print_calendar(year, month):
    for i in range(1, 30):
        print(f"{i} ", end="")
        if i % 7 == 0: # 7의 배수네??? 그럼 줄바꾸자...
            print("")

print_calendar(2024, 5)