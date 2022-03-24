
# 8-1 중첩 함수 global, nonlocal
# 전역변수
data = 10
def f1():
    print("f1 ", data)
print("--- Main call f1()")
f1()

# 변수범위 global
x = 20      #global
def func():
#    x = 10  #local
#    print("f.local:  ", x)
    global x
    x = 11
    print("f.global: ", x)
print("--- Main call func()")
func()
print("global: ", x)   #global

# 중첩함수 & nonlocal
def print_insa():
    insa = "Hello!!!"
    print("f.insa")
    def print_message():
        print("f.message: ", insa)

    print("f.insa call message()")
    print_message()

print("--- Main call insa()")
print_insa()

def A():
    x = 10
    print("f.A set x = ", x)
    def B():
        nonlocal x
        x = 20
        print("f.B set nonlocal x = ", x)
    B()
    print("f.A x?  : ", x)
print("--- Main call A()")
A()

def A():
    x = 100
    y = 500
    print("f.A set x,y : ", x, y)
    def B():
        x = 10  #local
        print("f.B set x :", x)
        def C():
            nonlocal x
            nonlocal y
            x += 50
            y += 200
            print("f.C nonlocal x+=50  : ", x)
            print("f.C nonlocal y+=200 :", y)
        print("f.B call C()")
        C()
    print("f.A call B() --- Before A.x,y ", x, y)
    B()
    print("f.A call B() --- After  A.x,y ", x, y)
print("--- Main call A()")
A()


