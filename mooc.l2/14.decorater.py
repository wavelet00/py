### 14 decorator @
#      ex) @staticmethod  @classmethod  @abstractmethod
print('>>> 14-1 without decorator ')
def trace(func):
    def wrapper():
        print('<tr ', func.__name__,'func start')
        func()
        print('>tr ', func.__name__,'func end')
    return wrapper
def hello():
    print('hello()')
def insa():
    print('insa()')

hello = trace(hello)
hello()

insa = trace(insa)
insa()

print('>>> 14-1 with decorator ')
def trace(func):
    def wrapper():
        print('<tr ', func.__name__,'func start')
        func()
        print('>tr ', func.__name__,'func end')
    return wrapper

@trace
def hello():
    print('hello()')
@trace
def insa():
    print('insa()')

#-- hello = trace(hello)
hello()
#-- insa = trace(insa)
insa()

print('>>> 14-2 decorator in func with args and return')
def trace2(func):
    def wrapper(a,b):
        r = func(a,b)
        print('{}:a={},b={}->{}'.format(func.__name__,a,b,r))
        return r
    return wrapper

@trace2
def sum(a,b):
    return a+b
print(sum(40,100))

def trace3(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('{0}(args={1},kwargs={2})->{3}'.format(func.__name__,args,kwargs,r))
        return r
    return wrapper
@trace3
def get_max(*args):
    return max(args)
@trace3
def get_min(**kwargs):
    return min(kwargs.values())
print(get_max(10,40,29,50,100))
print(get_min(x=10,y=40,z=5))

print('>>> 14-2 decorator class with __call__()')
class CTrace:
    def __init__(self,func):
        self.func = func
    def __call__(self):
        print(self.func.__name__,'Start')
        self.func()
        print(self.func.__name__,'Stop')
@CTrace
def insa():
    print('insa')
insa()


print('>>> 14-2 decorator class with __call__()')
class CTrace2:
    def __init__(self,x):
        self.x = x
    def __call__(self,func):
        def wrapper(a,b):
            r = func(a,b)*self.x
            print('{0}(a={1} b={2})->{3}'.format(func.__name__,a,b,r))
            return r
        return wrapper
@CTrace2(5)
def sum(a,b):
    return a+b
@CTrace2(10)
def subtract(a,b):
    return a-b
print(sum(20,40))
print(subtract(20,40))

