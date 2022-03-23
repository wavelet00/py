keys = ['a','b','c','d']
data1 = {k:v for k,v in dict.fromkeys(keys).items()}
print(data1)

data2 = {k:100 for k in dict.fromkeys(keys).keys()}
print(data2)

data3 = {'name':['kim','lee','choi']}
data4 = {v:0 for value in data3.values() for v in value }
print(data4)


words = 'have a good day'.split()
print(words)
ddata = {i:w for i,w in enumerate(words)}
print(ddata)

ddata2 = {'one':100, 'two':200, 'three':300}
del ddata2['two']
print(ddata2)

data5 = {'one':10, 'two':20, 'three':30, 'four':40}
for k,v in data5.items():
    if v == 20:
#        del data5[k]   # error occurred!!
        print(data5[k])

data5 = {k:v for k,v in data5.items() if v != 20}
print(data5)


