#region While문
# prompt = '''1.ADD   2. Del  3. List 4. Quit
# Enter number : '''

# number = 0
# while number !=4:
#     print(prompt, end = '')
#     number = int(input())
#endregion

#region for문 = for 변수 in 리스트/튜플/문자열
# # 2-1. 전형적인 for문
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# 2-2. for문과 range()함수 => 숫자 리스트를 자동으로 만들어주는 함수
#1 ~ 100까지의 합계
# sum = 0
# for i in range(1, 101) : 
#     sum += i
# print(f'1부터 100까지의 합계는 {sum} 입니다.')

# # 2-3. 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} X {j} = {i*j}')
#     print(" ")

# <연습문제> 사용자가 희망하는 단을 숫자로 받아서 
dan = int(input('원하는 단을 입력하세요!'))
for i in range(2, dan) :
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')




#endregion












