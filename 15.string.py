## translate
table = str.maketrans('aeiou','12345')
str1 = 'apple'.translate(table)
print(str1)

## join 
data = ['red','blue','green','yellow']
str2 = ''.join(data)
print(str2)
str3 = '-'.join(data)
print(str3)

## strip
str4 = '   hello python   '
print(str4.lstrip())
print(str4.rstrip()) # --> delete new line
print(str4.strip())
str5 = ',.hello world,.'
print(str5.lstrip(',.'))
print(str5.rstrip(',.'))
print(str5.strip(',.'))

## ljust, rjust, center, zfill
sdata = 'good day'
print(sdata.ljust(15))
print(sdata.rjust(15))
print(sdata.center(15))
sdata2 = '432'
print(sdata2.zfill(5))
print('53.56'.zfill(10))
print('string'.zfill(10))

### 15-2 regular expression
print('>>> 15-3 regular expression')
import re
rc = re.compile('hello')
rdata = re.match('hello','hello, world')
rdata = re.match(r'hello','hello, world')
rdata = re.match(rc, 'hello, world')
print(rdata)
print(rdata.span()[0])
print(rdata.span()[1])

print('>>> 15-3 regular expression - search')
robj2 = re.search('^hello','hello, world')
print(robj2)
robj3 = re.search('world$','hello, world')
print(robj3)
robj4 = re.match('world','hello, world')
print(robj4)
robj5 = re.search('hello|world','good world')
print(robj5)

### 15-4 regular expression
print('>>> 15-4 regular expression * +')
print(re.match(r'[0-9]*','121hello'))
print(re.match(r'[0-9]+','121hello'))
print(re.match(r'[0-9].','121hello'))
print(re.match(r'[0-9]','121hello'))

print(re.match(r'a*b','b'))
print(re.match(r'a+b','b'))
print(re.match(r'a*b','aab'))
print(re.match(r'a+b','aab'))

print('>>> 15-4 regular expression ? . {} ')
# ? : 0 or 1
print(re.match(r'ab?d','abd'))
print(re.match(r'ab.d','abcd'))

print(re.match(r'[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}','010-7777-7878'))
print(re.match(r'[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}','02-111-7878'))

print('>>> 15-4 regular expression [] eng, kor  ')
print(re.match(r'[a-zA-Z0-9]+','everyone5656'))
print(re.match(r'[가-]+','안녕하세요5656'))

print(re.match(r'[^A-Z]+','everyone5656'))
print(re.match(r'[^0-9]+','안녕하세요5656'))

print('>>> 15-4 regular expression \d, \D, \w, \W ')
print(re.match(r'\d+','342everyone'))     # \d number
print(re.match(r'\D+','everyone5656'))    # \D not number
print(re.match(r'\w+','342everyone'))     # \w char
print(re.match(r'\W+','()everyone5656'))  # \W not char
# ()  group 
m = re.match('([0-9]+) ([0-9]+)','10 2283')
print(m.group(1))
print(m.group(2))
print(m.group(0))
print(m.group())
print(m.groups())


print('>>> 15-4 regular expression findall(), sub()')
fdata = re.findall('[0-9]+', '12 22 4 string python 3 82')
print(fdata)
sdata=re.sub('apple|orange','fruit','apple box orange tree')
print(sdata)
sdata2=re.sub('[0-9]+','num','12 22 4 string pyton 3 82')
print(sdata2)

print('>>> 15-4 regular expression sub() with func or lamda')
def multiple(m):
    n = int(m.group())
    print(n)
    return str(n*10)
sdata3 = re.sub('[0-9]+', multiple, '12 22 4 string pyton 3 82')
print(sdata3)

sdata4 = re.sub('[0-9]+', lambda m:str(int(m.group())*10), '12 22 4 string pyton 3 82')
print(sdata4)


