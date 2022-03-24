def person_print(name, age, address):
    print('name:', name)
    print('age:', age)
    print('address:', address)
person_print('kim', 30, 'suwon')
person_print(name='lee', age=40, address='incheon')
person_print(age=40, address='incheon', name='lee')

data1 = {'name':'wcc','age':30, 'address':'seoul'}
person_print(name=data1['name'],age=data1['age'],address=data1['address'])
person_print(**data1)

def city_info(**data):
    print("f args ", data, type(data))
    for k,v in data.items():
        print("f arg  ", k,':',v)
    print()


city_info(seoul=90000, incheon=30230, busan=56222)
city_info(seoul=90000, busan=56222)
data2 = {'seoul':90000, 'suwon':32523, 'incheon':30230, 'busan':56222}
print("data2 : ", data2, type(data2))
city_info(**data2)

