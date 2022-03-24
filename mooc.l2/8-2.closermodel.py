## 클로저 정의
#  클로저는 함수 자신이 가지고 있는 환경을 저장한 정보이다.
#  클로저는 일반 함수와는 다르게, 자신의 영역 밖의 변숫값을 저장하고 자신의 정보를 참조할 수 있게 해준다.
#  클로저 조건은 아래와 같다.
#  - 중첩 함수를 갖는다.
#  - 중첩 함수는 자신을 감싸고 있는 함수 영역(부모함수)의 변수를 참조하고 있다.
#  - 부모함수는 중첩 함수(자식 함수)를 반환한다.

# 클로저 생성
def calc():
    x = 1
    y =30
    print("f.calc x,y : ", x, y)
    def c_func(input):
        print("f.calc.c_func x,y,input", x, y,input)
        return x + input * y
    return c_func
print("--- TEST closer with fuction calc, calc.c_func")
cal = calc()  # 메모리에 c_func,x,y 저장된 후 반환 된다, (클로저가 저장되어 이후 재사용 가능)
print(calc)
print(cal)
print(cal(2))
print(cal(4))
print(cal(6))

# lambda closer
def calc():
    x = 1
    y = 300
    print("f.calc x,y : ", x, y)
    return lambda input: x+input*y
print("--- TEST closer with fuction calc, calc.lambda")
cal = calc()  # 메모리에 c_func,x,y 저장된 후 반환 된다, (클로저가 저장되어 이후 재사용 가능)
print(calc)
print(cal)
print(cal(2))
print(cal(4))
print(cal(6))
print(calc()(10))

