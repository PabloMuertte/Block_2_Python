"""
Запись в файл
colors = ['red','green','blue123']
data = open('file.txt','a')
#data.writelines(colors) #разделителей не будет
data.write('Line 12\n')
data.write('Line 13\n') 
data.close()

with open('file.txt','w') as data:
    data.write('Line 2\n')
    data.write('Line 3\n') 

Вывод 
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit()

______________________
Импортирование функции из другого файла

import Siminar_1 as Sim

print(Sim.f(1))



def new_string(symbol,count = 3):
    return symbol * count

print(new_string('!', 5)) #!!!!!
print(new_string(4)) # 12


def concatenatio(*params):
    res: str = ""
    for item in params:
        res+= item
    return res

print(concatenatio('a','s','d','w'))

Числа фибоначи

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range (1,10):
    (fib(e))

print(list)

Кортежи
""" 
""" a=(3,1,41,4)
print(a)
print(a[0])

for item in a:
    print(item) 




t = tuple(['red','green','blue'])
red, green, blue = t    
print('r:{} g:{} b:{}'.format(red,green,blue))
"""

""" Словари 
dictionary = {}
dictionary = \
    {
        'up': '↑',
        'down':'↓',
        'left': '←',
        'right': '→'
    }

print(dictionary)

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(v)
"""

""" Множества 

colors={'red','green','blue'}

print(colors)
colors.add('grey')
print(colors)
colors.remove('red')
print(colors)
colors.clear()
print(colors)

a = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy()  #c= {1,2,3,5,8}
u = a.union(b) #u = {1,2,3,5,8,12,21}
i = a.intersection(b) #i = {8,2,5}
dl = a.difference(b) # dl = {1,3}
dr = b.difference(a) #dr = {13,21}

q = a \
    .union(b)\
    .difference(a.intersection(b))
#{1,21,3,13}
"""

""" Списки 

list1 = [1,2,3,4,5]
list2 = list1
list1[0] = 123
list2[1] = 23

for e in list1:
    print(e)

print()

for e in list2:
    print(e)


list1 = [1,2,3,4,5]


print(list1.pop(2))
print(list1)


list2 = [1,2,3,4,5]

print(list2.insert(2, 11))
print(list2)
"""

list2 = [1,2,3,4,5]

print(list2.append(11))
print(list2)