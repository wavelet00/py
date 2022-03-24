## 2-1
data1 = [10,20,30]
data1.append([100,200]) # add one object
print("1. append: ", data1, len(data1))

data2 = [100,200,300]
data2.extend([10,20])   # add two object
print("2. extend: ", data2, len(data2))


data3 = [10,20,30,40]
print("3. pop()   ", data3.pop())   # stack with pop & append
print("   ", data3)
print("3. pop(1)  ", data3.pop(1)) # queue
print("   ", data3)

## 2-2 copy
data1 = [0,0,0,0]
data2 = data1
print("2-2 '=' data1 is data2   : ", data1 is data2)
data2[2] = 99
print(data2, data1)

data3 = [0,0,0,0]
data4 = data3.copy()
print("2-2 'copy' data3 is data4: ", data3 is data4)
data3[2] = 99
print(data3, data4)


## 2-3 comprehension
data1 = []
for i in range(10):
    data1.append(i)
print("2-3 for       : ", data1)

data2 = [i for i in range(10) if i % 2 == 0]
print("2-3 [i for..  : ", data2)

data5 = []
for i in range(2,10):
    for j in range(1,10):
        data5.append(i*j)
print("2-3 for x2    : ", data5)

data6 = [ i*j for i in range(2,10) for j in range(1,10) ]
print("2-3 [i*j for..: ", data6)

data7 = [i if i%2 == 0 else 100 for i in range(10)]
print("2-3 [i.. else : ", data7)

