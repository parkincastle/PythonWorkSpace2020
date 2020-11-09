# 파이썬 내장 함수는 외부 모듈과 달리 import가 필요하다

#type(object) = > 자료형이 알려줌.
# print(type("abcd"))
# print(type(['abcd'])

# # id(object) => 객체의 주고 값 반환
# # a = 3
# # print(id(a))
# # print(type(a))

# #power(x, y) => x를 y만큼 제곱해서 값을 반환
# print(pow(3, 4), pow(2, 3))

# # sum(iterable) => 합계 반환
# print(sum(1, 2,3 ,4,5)), sum({1, 2, 3})

# max(열거형 자료), min(열거형 자료)
#print(max)

# #round(number)  =>반올림 수 반환
# print(round(4.6))
# print(round(4.1))
# print(round(3.141592, 3))

# #eval(계산 가능한 문자열) => 문자열을 계산한 결과값 반환
# print(eval('1+2'))

# #list(열거형 자료) => 리스트 반환
# print(list('python'))
# print(list(1, 2, 3))

# #filter(함수, 열거형 자료) => 열거형 자료가 주어진 함수에서 실행되었을때 참인 값만 반환
# def postiive(n):
#     return n>0

# map(함수ㄹ, 열거형 자료) => 함수f가 수행한 결과를 반환
def two_times(x):
    return x*2

print(list(map(two_times, [1,2,3,4])))
print(list(map(lambda x: x*2, [1,2,3,4])))

#range([start], stop, [step]) = > 입력받은 숫자에서 반복 가능한 객체 반환
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(1, 10, 2)))

# sorted(열거형 자료)
print(sorted([3,1,2])) # [1, 2, 3]
print(sorted('zero')) # ['e', 'o', 'r', 'z']



