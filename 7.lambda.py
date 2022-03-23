def plus_ten(x):
    return x + 10
print(plus_ten(10))

## lambda expression == 'anonymous function'
#  lf = lambda argument : return_val    # lf <- function address
lf = lambda x : x+10
print(lf(10))

# invalid syntax with using valiable definition in return expression
#print((lambda x : y=10 x+y)(10))
y=20
print((lambda x : x+y)(5))

## lambda & map
def plus_ten(x):
    return x + 10
d1 = [5,2,8,9]
data1 = list(map(plus_ten, d1))
print(data1)
data2 = list(map(lambda x : x+10, d1))
print(data2)

a = list(range(1,11))
data1 = list(map(lambda x : str(x) if x % 3 == 0 else x, a))
print(data1)

## lambda multi objects
data1 = [1,2,3,4,5]
data2 = [20,40,50,50,80]
print("lambda multi objects: ", list(map(lambda x,y: x*y, data1, data2)))

## lambda filter
def f(x):
    return x>5 and x<10
data = [8,3,2,10,15,7,1,9,0,11]
result1 = list(filter(f, data))
result2 = list(filter(lambda x: x>5 and x<10, data))
print("filter() :", result1, result2)

## lambda reduce
from functools import reduce
def f(x,y):
    print("f(x,y):", x,y)
    return x+y
data = [1,2,3,4,5]
print("reduce with func   - ", "in: ", data, "out: ", reduce(f,data))
print("reduce with lambda - ", "in: ", data, "out: ", reduce(lambda x,y:x+y, data))

