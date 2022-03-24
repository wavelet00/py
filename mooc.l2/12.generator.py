### 12-1 generator : creat interator
##  yield = generator
print('12-1 generator yield')
def number_generator():
    yield 0
    yield 1
    yield 2
for i in number_generator():
    print(i)

print('12-1 generator yield & __next__()')
g = number_generator()
print(g.__next__())   # yield 0
print(g.__next__())   # yield 1
print(g.__next__())   # yield 2
#print(g.__next__())   # --> StopIteration 

# for __iter()__ -> __next__()  yield 0 -> return 0 & wait
#                -> __next__()  yield 1 -> return 1 & wait
#                -> __next__()  yield 2 -> return 2 & wait
#                -> __next__()  StopIteration -> end function 

## creat generator  --> simplify iterator class
print('12-2 creat generator')
def CRange3(stop):
    n = 0
    while n < stop:
        yield n
        n+=1
for i in CRange3(3):
    print(i)

def strdata_upper(datas):
    for str in datas:
        yield str.upper()
foods = ['juice','steak','bread','coffee']
for data in strdata_upper(foods):
    print(data)

## yield from --> send data in one time without calling yield several times 
print('12-2 yield from -- ex1 ')
def multiple_number_generator():
    data = [10,20,30,40]
    print('m yield from ', data)
    yield from data
for idata in multiple_number_generator():
    print('--for loop ', idata)

print('12-2 yield from -- ex2')
def n_generator(stop):
    n = 0
    while n < stop:
        print('n_g yield ', n)
        yield n
        n+=1
def t_generator():
    print('t_g yield form ')
    yield from n_generator(3)
for i in t_generator():
    print('--for loop  ', i)
