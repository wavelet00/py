### 11-1 iterator
#   for i in [1,2,3,4]
iterator = [1,2,3,4].__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
#print(iterator.__next__())  # --> StopIteration occurred
#   for i in range(4) 
iterator = range(4).__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
#print(iterator.__next__())  # --> StopIteration occurred

## 11-2 iterator creat
print('11-2 iterator class')
class CustomRange:
    def __init__(self,start,stop):
        self.current = start
        self.stop = stop
        print('0init ',self, start,stop)
    def __iter__(self):
        print('0iter ',self)
        return self
    def __next__(self):
        print('0next ',self)
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

for i in CustomRange(0,4):
    print(i)

print('11-2 iterator class - unpack')
num1, num2, num3  = CustomRange(0,3)
print(num1,num2,num3)

print('11-2 iterator class - map')
#num1, num2 = map(int, input().split())

print('11-2 iterator class - indexing')
class CustomRange2(CustomRange):
    def __init__(self,start,stop):
        print('1init ',self, start,stop)
        self.stop = stop
        super().__init__(start,stop)
    def __getitem__(self,index):
#        print('1getitem ',self, index, super(), super().self)
#        if index < super().self.stop:
        if index < self.stop:
            return index
        else:
            raise IndexError
print(CustomRange2(0,3)[1])
print(CustomRange2(0,3)[2])
print(CustomRange2(0,3)[0])

