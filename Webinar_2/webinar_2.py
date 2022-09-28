"""
Напишите программу, которая принимает на вход число N 
и выдает последовательность из N членов. (умножаем на -3)
Пример:
Для N = 5; 1, -3, 9, -27, 81.
"""
"""
a = int(input('Please input your number : '))
i= 0
a_sum = 1
txt='1'
while i<a-1:
    a_sum = a_sum*-3
    i= i+1
    txt= txt + ' ' + str(a_sum)
print(txt)

n = int(input('Please insert your number :'))
j =1
for i in range(1,n+1):
    print(j,end= " " )
    j = j *-3 

n = int(input('Please insert your number :'))
j = 1
list1 =[]
for i in range (1, n+1):
    list1.append(j)
    j=j*-3
print(list1)

n = int(input('Please insert your number :'))
j = 1
list1 =[]
for i in range (1, n+1):
    list1.append(str(j))
    j*=-3
print(", ".join(list1))
"""

"""
Напишите программу, в которой пользователь будет задавать две строки,
а программа будет определять количество вхождений(соответствий) одной
строки в другую.

str_1 = str(input("Please insert your string: "))
str_2 = str(input('Please insert second string: '))

print(str_1.count(str_2))
"""

"""
Для натурального N создать словарь индекс-значение, состоящий из элементов
последовательности 3N+1.
Пример:
Для N =6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input ('Please input your number: '))
d = dict() # d= {}
j = 1
for i in range(n):
    d[j] = 3 * j + 1
    j+= 1
print(d)
"""


