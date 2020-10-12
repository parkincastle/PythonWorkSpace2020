## 파이썬 예외 처리
# 1. 에러가 발생하는 경우 프로그램은 중지
# n = 4/0

#region try, except문 기본 구조
# try:
#     오류가 날 것 같은 실행문장
# except 발생 에러 as 변수:
#     pass

# 2. try, except문을 통해 에러가 발생해도 프로그램이 중지되지 않도록 한다.
try:
    n = 4/0
except :
    pass # 아무것도 안하고 넘어감

# 3. ZeroDivisionError 예외 처리
try:
    n = 4/0
except ZeroDivisionError as err:
    print(f"0으로 나눌수 없습니다. :  {err}")

# 4. IndexError 예외처리
try:
    a = []
    a[0] = 100
except IndexError as err:
    print(f"인덱싱 에서 발생 : {err}")

# 5. Exception 예외 처리
try:
    n = 4/0
    a = []
    a[0] = 100
except Exception as err:
    print(f"에러 발생 : {err}") #먼저 발생하는 에러 처리

# 6.try - except ~ finally
#에러 발생여부 상관없이 실행해야하는 코드를 finally문 안에 넣는다.
try:
    # f = open('readme.txt', mode = 'r', encording = 'urf - 8')
    f = open('새파일.txt', mode = 'r', encoding='urf - 8')
except Exception as err:
    print(f"에러 발생 : {err}")
finally:
    print('finally문 실행')

# 7.여러개의 오류처리
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as err:
    print('ZeroDivisionError 발생')
except IndexError as err:
    print('IndexError 발생')
except Exception as err:
    print(f"에러 발생 : {err}")

try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as err:
    print('ZeroDivisionError, IndexError 발생')
except Exception as err:
    print(f"에러 발생 : {err}")















print("마지막 코드")