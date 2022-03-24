def print_nums(a,b,c):
    print('f: ', a,b,c)

print_nums(10,40,70)


data1 = [10,20,30]
print_nums(data1[0], data1[1], data1[2])
print("data1: ", *data1)
print_nums(*data1)

def add(*data):
    print("f: ", type(data))
    result = 0
    for d in data:
        result += d
    return result

print("add() : ", add(10,20))
print("add() : ", add(10,20,30,40))
x = (40,50,70)
print("add(*x) : ", add(*x))


