
data1 = {'name':'kim', 'age':20, 'address':'seoul'}
print("{k:v} -> ", data1, type(data1))

data2 = {'names':['kim','lee','choi'],
        'info':{'ages':[10,20,30], 
                'height':[180,172,158]
               }
        }
print(data2)

data3 = {10:[40,50], True:[22.2,444.56], 3.3:['kim','choi']}
print(data3)
print(data3[10])
print(data3[True])
print(data3[3.3])

data4 = dict(name='kim', age=30)
print("dict() -> ", data4, "[name] -> ", data4['name'])

data5 = dict(zip(['health','name'],[100,'kim']))
print("dict(zip(typle)) -> ", data5)

data6 = dict([('name','lee'),('age',50),('weight',80)])
print("dict(list) -> ", data6)

data7 = {'age':30}
print(data7)
data7['age'] = 50
print(data7)
data7['weight'] = 80
print(data7)

data7 = {'age':30}
data7.setdefault('height',180)
print("setdefault() - ", data7)
data7.setdefault('info')
print("setdefault() - ", data7)

data8 = {'name':'lee','age':20}
data8.update(name=40)
print(data8)

data8.update(weight=78)
print(data8)

keys=['a','b','c','d']
data1 = dict.fromkeys(keys)
print("fromkeys(keys)     -> ", data1)
data2 = dict.fromkeys(keys,100)
print("fromkeys(keys,100) -> ",data2)

## 중첩딕셔너리 복사 --> deepcopy 
import copy 
data7 = {'a':{'name':'kim'},'b':{'name':'choi'}}
print(data7)
data8 = copy.deepcopy(data7)
data8['a']['name'] = 'lee'
print(data8)
