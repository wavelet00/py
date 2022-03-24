### 13 coroutine
#    main routine -- sub routine --> if sub routine ends, it is deleted in memory
#    cooperative routine --> has multiple entry point
## send coroutine value :  main - 'send(value)' - rx value in coroutine to ' (yield) '
print('>>> 13 coroutine send & (yield) - wait&receive')
def number_coroutine():
    while True:
        x = (yield)
        print(' coroutine rx ', x)
co = number_coroutine()
next(co)
co.send(1)
co.send(2)
co.send(3)
co.close()

print('>>> 13 coroutine yield valiable - return and wait&receive')
def number_coroutine2():
    total = 0
    while True:
        print(' coroutine before rx total  ', total)
        x = yield total     # return total to main, and wait value from main
        total+=x
        print(' coroutine after  rx ', x, total)
co = number_coroutine2()
print('main next ', next(co))      # get total 0 from coroutine 'yield total'
print('main send(1) ', co.send(1)) # send 1 to coroutine x, and get total from coroutine 'yield total' and print it.
print('main send(2) ', co.send(2))
print('main send(3) ', co.send(3))
#co.close()

## coroutine exception handling
#  main call close(), GeneratorExit Exception occurred in coroutine
print('>>> 13 coroutine exception handling')
def number_coroutine3():
    try:
        while True:
            x = (yield)
            print(' -- co rx ', x)
    except GeneratorExit:
        print('coroutine end!!!')
co = number_coroutine3()
next(co)
for i in range(5):
    print('send i ',i, co.send(i))
print('close ', co.close())


print('>>> 13 coroutine exception handling')
def number_coroutine4():
    total = 0
    try:
        while True:
            x = (yield)
            total += x
            print(' -- co rx ', x)
    except RuntimeError as e:
        print(e)
        yield total

co = number_coroutine4()
next(co)
for i in range(20):
    print('send i ',i, co.send(i))
#print('close ', co.close())
print('close ', co.throw(RuntimeError, 'close coroutine with exception forcely'))

print('>>> 13 sub coroutine and yield from')
def accumulate():
    total = 0
    print('   -- acc start ', total)
    try:
        while True:
            x = (yield)
            print('   -- acc rx x ', x)
            if x is None:
                print('   -- acc total ', total)
                return total
            total+=x
    except GeneratorExit:
        print('   -- coroutine1 end!!! acc')
def sum_coroutine():
    print(' -  sum start ')
    try:
        while True:
            total = yield from accumulate()
            print(' -  sum rx total ',total)
    except GeneratorExit:
        print(' - coroutine2 end!!! sum')

print('before co ')
co = sum_coroutine()
print('co created, before next ')
print('next ', next(co))
for i in range(3):
    print('ready to send i ', i)
    #print('send i ',i, co.send(i))
    co.send(i)
print('send(None) to exit ', co.send(None))

for i in range(1,11):
    #print('send i ',i, co.send(i))
    co.send(i)
print('send(None) to exit ', co.send(None))
print('close ', co.close())

