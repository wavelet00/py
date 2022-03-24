### 10-1 Class Inherit
#   base class - drived class

class Person:
    def insa(self):
        print('Person hello')

class Student(Person):
    def study(self):
        print('Student Studying...')

obj1 = Student()
obj1.study()
obj1.insa()

## super() : get address of parent class
class AAA:
    def __init__(self):
        print('AAA init method')
        self.message = 'hi everyone'
class BBB(AAA):
    def __init__(self):
        super().__init__()    # if delete this line, error is occured !!! 
        print('BBB init method')
        print(self.message)

obj1 = BBB()

## overriding 
class Student2(Person):
    def insa(self):             # override insa() against Person.insa()
        super().insa()
        print('Student2 Studying...')
obj1 = Student2()
obj1.insa()

# abstract class
from abc import *
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    @abstractmethod
    def gotoSchool(self):
        pass

class Student(StudentBase):
    def study(self):
        print('Studying ...')
    def gotoSchool(self):
        print('Going to school ...')

class Student__(StudentBase):
    def test(self):
        print('Student__ test')

obj1 = Student()
obj1.study()
obj1.gotoSchool()
obj2 = Student__()   # -->   TypeError: Can't instantiate abstract class Student__ with abstract methods gotoSchool, study
obj2.test()
