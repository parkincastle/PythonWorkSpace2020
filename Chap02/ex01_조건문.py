#region if ~ else문
#num = int(input('정수를 입력하세요 : ')) #형 변환

# # 1. num이 짝수인지 홀수인지 출력
# if num % 2 == 0 :
#     print('짝수 입니다.')
# else:
#     print('홀수 입니다.')

# 2. num이 양수인지 검사하고, 짝수/홀수 출력
# if num > 0 :
#     if num % 2 == 0 :
#         print('짝수 입니다.')
#     else:
#         print('홀수 입니다.')
# else:
#     print("양수 입력!")

# 3. 택시 탁승(현금 또는 카드 보유 체크)
# card = False
# money = 2000

# if money >= 3000 or card:
#     print('택시 탑승 가능')
# else:
#     print('택시 탑승 불가늘')

# 4. x in 리스트/튜플/문자열
# pocket = ['paper', 'cellphone', 'money']

# if money >= 3000 or pocket:
#     print('택시 탑승 가능')
# else:
#     print('택시 탑승 불가늘')

# # 5.elif
# pocket = ['paper', 'cellphone', 'money']
# card = True

# if 'money' or pocket:
#     print('돈이 있음')
# elif :
#     print('카드있음')
# else:
#     # print('아무것도 없음')

# 6. 조건부 표현식
score = int(input('당신의 점수는?'))

if score >= 60:
    message = 'sucess'
else:
    message = 'failure'

message = 'sucess' if score >= 60 else 'failure'

print(message)



