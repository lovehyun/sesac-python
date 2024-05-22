# 레거시한 코딩 스타일
def remove_duplicate(numbers):
    unique_list = [] # 1,2,3,4

    for n in numbers: # 3 (다섯번째 3)
        duplicate_check = False # 중복 안될꺼야~~
        
        for u in unique_list: # 1,2,3,4
            print(f'입력값:{n}, 유닉목록:{u}')  # 3,1  # 3,2  # 3,3

            if n == u:
                print(f'중복: {n} == {u}')
                duplicate_check = True   # 어?? 중복 되었음...
                break

        if not duplicate_check:  # 중복이 아니면???
            print(f'중복아닌것:{n}')
            unique_list.append(n)

    return unique_list

# 조금 더 파이썬 스러운 스타일
def remove_duplicate2(numbers):
    unique_list = []

    for n in numbers:
        if n in unique_list:
            pass
        else:
            unique_list.append(n)

    return unique_list

# 조금 더더더 파이썬 스러운 스타일 (*** 가장 실무적인 코드 ***)
def remove_duplicate3(numbers):
    unique_list = []

    for n in numbers:
        if n not in unique_list:
            unique_list.append(n)

    return unique_list

# 모던 파이썬 코드
def remove_duplicate4(numbers):
    return list(set(numbers))

numbers = [1,2,3,4,3,2,1,5,6,7,6,5]
unique_numbers = remove_duplicate4(numbers)

print("원본 리스트: ", numbers)
print("유닉 리스트: ", unique_numbers)
