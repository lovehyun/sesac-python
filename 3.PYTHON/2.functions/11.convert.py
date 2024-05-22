# 1. 문자를 입력받아, 대소문자를 변경하시오.
#  문자내의 대문자->소문자, 소문자->대문자
#  예) HellO => hELLo
# 신입개발자 코드 (파이썬 ~1년차)
def convert_case(text):
    converted_text = ""

    for char in text:
        if char.islower():
            # converted_text += char.upper()
            converted_text = converted_text + char.upper()
        elif char.isupper():
            converted_text += char.lower()
        else:
            converted_text += char

    return converted_text

print(convert_case('HellO'))
print(convert_case('WelCOME'))
print(convert_case('GoodBye'))
print(convert_case('Good bye'))
print(convert_case('This is long message. haha1234'))

def convert_case2(text):
    return ''.join([char.upper() if char.islower() else char.lower() for char in text])

# for char in text # text를 읽어서 char 추출한다
# 맨 앞에 char 는 for 문의 결과 char가 담기는곳.
#         char.upper()
#         char.lower()
# if 구문의... char.upper() 를 하기 위한 조건


print(convert_case2('HellO'))
