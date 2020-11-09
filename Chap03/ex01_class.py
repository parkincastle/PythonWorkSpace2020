#region 매개변수가 없는 생성자
# class Calculator1 : 
#     # 생성자 : 클래스를 생성하는 함수
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

# # 객체 생성
# calc1 = Calculator1()
# calc2 = Calculator1()

# print(calc1.add(1))  # 1
# print(calc1.add(2))  # 3
# print(calc1.add(3))  # 3
# print(calc1.add(4))  # 7



#endregion

#region 매개변수가 있는 생성자를 가진 클래스
# 덧셈을 수행하는 객체 또는 곱셈을 수행하는 객체
# class Calculator2:
#     def __init__(self, operator):
#         self.operator = operator

#     def calc(self, *args) :  # *args => 여러개의 인자를 튜플로 받는 매개변수
#         self.result = 0
#         if(self.operator == 'add'):
#             # 모든 args값 덧셈수행
#             for i in args:
#                 self.result += i
#         elif(self.operator == 'multiply'):
#             self.result = 1
#             # 모든 args값 곱셈 수행
#             for i in args:
#                 self.result *= i
#         


# calc3 = Calculator2('add')
# print(calc3.calc(1,2,3,4,5))
# print(calc3.result)

# calc4 = Calculator2('multiply')
# print(calc3.calc(1,2,3,4,5))
# print(calc3.result)

#endregion

#region 사칙연산 클래스
# 생성자에 숫자 두개를 받아서, 사칙연산 메소그를 수행하는 클래스 add, substract, multiply, divide
class Calculator3:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def substract(self):
        return self.num1 - self.num2

    def  multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

calc = Calculator3(3, 4)
# print(calc.add())
# print(calc.substract())
# print(calc.multiply())
# print(calc.divide())
#endregion

#region 상속
class ExtendedCalculator(Calculator3):
    def pow(self):
        return self.num1 ** self.num2


calc = ExtendedCalculator(2,4)
print(calc.add())
print(calc.substract())
print(calc.multiply())
print(calc.divide())
print(calc.pow())

#endregion

#region 메서드오버라이딩
class SafeCalculator(Calculator3):
    def divide(self):
        if self.num2 == 0:
            return '0으로 나눌수 없습니다.'
        else:
            return self.num1 / self.num2

# calc = SafeCalculator(5, 0)
# print(calc.divide())

# calc = SafeCalculator(5, 2)
# print(calc.divide())



#endregion

#region class 변수
class Family:
    lastname = '박'

    def __init__ (self, firstname):
        self.firstname = firstname


insung = Family('인성')
print(f"{insung.lastname}{insung.firstname}")



#endregion






