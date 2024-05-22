def hello():
    print('hello1')
    print('hello2')
    print('hello3')

# hello()


def numbers(num1):
    result = num1 + 4
    if result < 10:
        return result

num1 = numbers(3)
num2 = numbers(9)

print(num1)
print(num1, num2)

# ----------------------

# 미션1. 덧셈을 하는 함수를 작성하시오.
#    숫자 두개를 입력 받아서, 해당 숫자의 합산을 반납한다.

def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(3,5))
print(add(10,20))


def add2(num1, num2):
    return num1 + num2

print(add2(2,3))

def add3(num1, num2):
    return num1, num2, num1+num2

print(add3(1,2))

# 미션2. 덧셈함수 만들었으니... 뺄셈, 곱셈, 나눗셈 함수도 보기...
#   모두다 덧셈처럼 2개의 인자를 입력받아, 하나의 결과를 반환하시오

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2


print(sub(5,3))   # 2
print(mul(2,3))   # 6
print(div(5,3))   # 1.66667


print(sub(5,0))   # 5
print(mul(2,0))   # 0
print(div(5,0))   # 5 나누기 0 

