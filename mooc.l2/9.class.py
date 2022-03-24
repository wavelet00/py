## 9-1 클래스 일반
## 객체 지향 프로그래밍
#  객체 지향 프로그래밍은 함수처럼 어떤 단순 기능만 사용하는 것이 아니라, 
#  기능 여러 개를 묶고 여러 데이터를 하나의 클래스에 넣어 다른 프로그래머가 재사용할 수 있도록 하는 것이다.
## class
#  클래스는 객체를 생성하기 위한 기본 정보(데이터,함수)를 가지고 있는 코드
#  클래스 객체를 생성하기 위한 설계코드로 얘기할 수 있다
#  클래스를 이용하여 생성되는 객체를 다른 이름으로 인스턴스(instance)라고 한다

## 클래스 구현
#  클래스 선언 기본 형식
#     class Persion(object) :
#  Class 예약어로 클래스 정의를 시작한다
#  소괄호는 상속 받을 클래스 이름을 넣으면 된다.
## 멤버 변수
#  멤버 변수를 선언하기 위해서는 __init__()를 사용한다
#  self 변수는 클래스로 생성된 인스턴스 주소 정보이다. (내부참조 기준 주소)
#  self 뒤의 매개변수들은 실제로 클래스가 가지게 되는 멤버 변수이다.
## 멤버 함수
#  멤버 함수는 클래스의 다양한 동작을 정의할 수 있다.

## 인스턴스
#  클래스에서 인스턴스를 생성하는 방법은
#  먼저 클래스 이름을 사용하여 __init__() 함수의 매개변수에 맞추어 값을 입력
#     pobject = Person() :
#  인스턴스(객체)의 속성에 접근하기 위해서는 .을 이용

print("> 9-1 class ")
class Person:
    def __init__(self):
        print("init_call")
        self.name = "kim"
        self.address = 'seoul'
    def print_info(self):
        print('name:{} address:{}'.format(self.name, self.address))

pObject = Person()
print(pObject.name)
print(pObject.address)
pObject.print_info()

class Test:
    def print_info2(self):
        print('test self : ', self)

pObj = Test()
print(Test)
print(pObj)
pObj.print_info2()
#print(pObj.print_info2())

## 9-2 클래스 속성
## 클래스 속성 (접근 시 self 사용할 수 있지만 정확한 표현은 클래스 이름을 사용하는 것)
print("> 9-2 class valiable ")
class Student:
    bag = []  # class valiable --> *** global in all class instances
    def __init__(self, name):
        self.name = name
        self.bag2 = []
        print("__init__ Student(name): ", name, " ,Class valiable bag : ", Student.bag, "bag2 ", self.bag2)
    def insert_bag(self, stuff):
        print("Student.insert_bag(stuff) ", stuff, self.name)
        self.bag.append(stuff)
        self.bag2.append(stuff)
    def bag_info(self):
        print("Student.bag_info - self.bag ", self.bag, " bag2", self.bag2, " in name ", self.name)
        print("Student.bag_info - Studen.bag ", Student.bag, " in name ", self.name)
hong = Student('hong')
print(hong, hong.insert_bag('book'))
hong.bag_info()
yun  = Student('yun')
print(yun, yun.insert_bag('pencil'))

hong.bag_info()
yun.bag_info()


## 9-3 정적 메소드, 클래스 메소드
## 정적 메소드
#   @staticmethod 키워드 사용
#   선언과 동시에 메모리에 올라가 사용 가능, 매개변수에 self를 지정하지 않는다.
#   인스턴스 속성에 접근할 수 없다
#   인스턴스와 관계없이 공통 목적으로 사용하는 메소드 만들때 사용.
print("> 9-3 staticmethod ")
class Calc:
    @staticmethod 
    def plus(a,b):
        print(a+b)
    @staticmethod
    def multi(a,b):
        print(a*b)
Calc.plus(10,20)
Calc.multi(10,20)

## 클래스 메소드 
class Car:
    count = 0
    def __init__(self):
        Car.count += 1
    @classmethod
    def maked_car_count(cls):
        print('{} cars are maunufactured'.format(cls.count))
c1 = Car()
c2 = Car()
Car.maked_car_count()

