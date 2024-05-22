x = 50

if x < 10:   # 이 조건이 True일때...
    print('x가 10보다 작습니다')
else:    # 위 조건이 False 일때....
    print('x가 10보다 큽니다')

#---------------------

score = 92

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(score, grade)

print("Score: {}, Grade: {}".format(score, grade))

print("Score: {0}, Grade: {1}".format(score, grade))
print("Score: {1}, Grade: {0}".format(score, grade))


print('점수는 {score} 이고, 성적은 {grade} 입니다')  # 문자열
print(f'점수는 {score} 이고, 성적은 {grade} 입니다') # 포멧팅


math = 90
eng = 90

if math >= 90 and eng >=90: # 가운데 조건을 and/or 로 바꿔가면서..
    print('졸업조건 충족\t\t\t안녕히가세요')
else:
    print('졸업 미흡')


