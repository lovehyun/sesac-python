import random

# 미션1. 랜덤 숫자 1~100까지를 생성하는 함수를 찾아서 출력하시오
# print(random.randint(1,100))


# 미션2. 주사위를 던지는 함수를 작성하시오
def roll_dice():
    return random.randint(1,6)
    
print("주사위를 던진 결과는: ", roll_dice())

# 미션3. 리스트에서 랜덤으로 요소를 선택하기
# 직접 for 로 구현해도 되지만........ 이런걸 해주는 라이브러리가 있음.
elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']
def choose_random_element(elements):
    # random_index = random.randint(0, len(elements) - 1)
    # print(random_index)
    # return elements[random_index]
    return random.choice(elements)


print("당신이 선택한 상품은: ", choose_random_element(elements))

# 미션4. 램덤으로 숫자 리스트 섞기
elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']
numbers = [1, 2, 3, 4, 5]
def random_list(elements):
    random.shuffle(elements)
    return elements

print('원본 리스트1: ', elements)
print('원본 리스트2: ', numbers)
print('섞인 리스트1: ', random_list(elements))
print('섞인 리스트2: ', random_list(numbers))

# 5. 랜덤으로 문자열 생성 (영문 대문자 6자리)


# 6. 랜덤 초이스에서 가중치를 고려한 랜덤 


# 7. 램덤 비밀번호 생성 (대소문자, 숫자포함 8자리)


# 8. 강력한 비밀번호 생성 (대문자, 소문자, 숫자를 각각 최소 1개이상 포함하는 8자리를 만들려면??)


