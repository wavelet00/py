data1 = 38,21,53,62,19
print(type(data1))
print("index() : ", data1.index(53))

data1 = 39,21,53,62,19,53
print(type(data1))
print("count() : ", data1.count(53))

data3 = 38,21,53,62,19
for i in data3:
    print("item : ", i, end=' ')

data10 = ()
data10 = tuple(i for i in range(10) if i%2==0)
print("tuple comprehension : ", data10)
data2 = (i for i in range(10) if i%2==0)
print("tuple comprehension : ", data2)

data1 = [1.2,2.5,3.7,4.6]
for i in range(len(data1)):
    data1[i] = int(data1[i])
print("for: ", data1)
data2 = [1.2,2.5,3.7,4.6]
#data2 = map(int, data2)
data2 = list(map(int, data2))
#data2 = tuple(map(int, data2))
print("map: ", data2)

def multi_ten(x):
    return x*10;
data = [4,2,6,8,9]
print("map: ", list(map(multi_ten, data)))

data3 = input().split()
print("input: ", data3)
data4 = list(map(int, input().split()))
print("input.map: ", data4)

data5,data6 = list(map(int,input().split()))
print("map unpack: ", data5,data6)
