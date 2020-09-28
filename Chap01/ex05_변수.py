# 변수가 저장한 메모리 주소 값 확인하기
a = [1, 2, 3]
print(id(a)) #24638696

#region
# #얉은 복사
# b = a
# print(id(b)) #24638696

# b.append(4)
# print(a, b) #[1, 2, 3, 4] [1, 2, 3, 4]
# print(f'a is b : {a is b}') # a == b : True
# print(f'a == b : {a == b}') 

# #깊은 복사
# a = [1,2,3]
# b = a[:] # 통째로 다 기지고 온다

# print(f'a is b : {a is b}')  #주소 비교
# print(f'a == b : {a == b}')  #값 비교

# print(a, b)
# b[0] = 10
# print(a, b) #[1, 2, 3] [10, 2, 3]
#endregion

#region 변수를 만드는 여러가지 방법
a, b = ('python', 'life') #튜플로 여러개의 값을 저장할수있다.
print(a, b) # python life

a, b = 'node', 'js' # 투플은 괄호생략 가능
print(a, b) #node js

[a, b] = ['python', 'life']
print(a, b) # python life

a = b = 'node.js'
print(a, b) # node js
#endregion

