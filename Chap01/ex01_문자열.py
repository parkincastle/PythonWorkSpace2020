### 문자열 ###
# food = 'Python\'s favorite food is perl'
# say = "\"python is very easy.\" he says."

# #여러 줄의 문자열을 변수에 대입하고 싶을때#
# multiline = "Life is too short\nYou need python"
# print(multiline)

# multiline = """Life is too short
# You need python"""

# print(multiline)

#region문자열 연산하기
# head = "Python"
# tail = 'is fun!'
# print(head + tail) # "Python is fun!"

# #2.문자열 곱하기
# print((head + '\n') * 5)

# #문자열 길이구하기
# print(len(head))

#endregion

#region 문자열 인덱싱 슬라이싱
#1.문자열 인덱싱
# str = "Life is too short, You need Python"
# print(str[3])  #e
# print(str[-1]) #n
# print(str[-2]) #o

# #2.문자열 슬라이싱
# print(str[0:6]) #Life i
# print(str [:6]) #Life i
# print(str[5:])  #is too short, You need Python
# print(str[19:-7]) #
#endregion

#region 문자열 포매팅(Formating)
# print("I eat %d apples" % 3)
# print("I ate %d apples. so I was sick for %s days." % (3, 'three'))

# #format 함수를 이용한  포매팅
# print("I eat {0} apples" .format(3))
# print("I ate {0} apples. so I was sick for {1} days." .format(3, 'three'))

# # f 문자열 포매팅(3.6 이상 버전부터 사용가능)
# name = '홍길동'
# age = 30
# print(f"나의 이름은 {name} 입니다. 나이는 {age} 입니다.")
#endregion

#region문자열 관련 함수글
#문자 개수 세기(count)
str = 'hobby'
print(str.count( 'b'))  #2

# 위치 알려주기
str = 'python is the best choice'
print(str.find('b'))    #14
print(str.find('h'))    #3
print(str.find('k'))    # -1

#대문자 바뀌기
print(str.upper())  #PYTHON IS THE BEST CHOICE
print(str.lower())  #python is the best choice

#공백 지우기
str = ' hi '
print(str)
print(str.lstrip()) # 왼쪽 공백 제거
print(str.rstrip()) # 오른쪽 공백 제거
print(str.strip())  # 양쪽 공백 제거

#문자열 바꾸기
str = 'Life is so short'
print(str.replace('short', 'long')) #Life is so long

#문자열 나누기 -> list로 변환
print(str.split()) #['Life', 'is', 'so', 'short']

str2 = 'a:b:c:d'
print(str2.split(':')) #['Life', 'is', 'so', 'short']

#endregion




