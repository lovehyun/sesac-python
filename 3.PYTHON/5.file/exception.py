def div(a, b):
    try:
        result = a / b
        print("실제결과는: ", result)
    except Exception as e:
        print("알 수 없는 오류가 발생하였습니다. 오류코드: ", e)
        return "NaN"
    
    return result

# print(div(5,3))
print(div(10, 0))
# print(div(10,'a'))
# print(div(15, 5))


# 문자숫자를 받아서 -> 숫자로 변환하기
# "20" => 20
def convert_to_interger(num_str):
    try:
        result = int(num_str)
    except ValueError:
        print("유효한 숫자를 입력하세요.")
        return None
    
    return result


print(convert_to_interger("20"))
print(convert_to_interger("100"))
print(convert_to_interger("a"))
