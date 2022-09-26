"""
a = int(input('Input your first digit: '))
b = int(input('Input your second digit: '))
result = (a == b**2 or b == a**2)
print(result)
"""

""" Напишите программу которая на вход принимает 5 чисел (можно списком) и находит максимальное из них.
    Примеры:
    1. 1, 4, 8, 7, 5 > 8
    2. 78, 55, 36, 90, 2 > 90
_______________________________________
max_n = 0
list = [1, 4, 8, 17, 5 ]
# list = [78,55,36,90,2]
for i in list:
    if max_n < i: 
        max_n = i
        i+1
print(max_n)
"""

""" Напишите программу, которая будет на вход 
принимать число N и выводить числа от -N до N
______________________________________________

a = int(input('Input your digit: '))
a_negative = a * -1
i = a_negative #max count
while i <= a:
    print(a_negative)
    i=i+1
    a_negative = a_negative+1


a = int(input('Input your digit: '))
s = ''
for i in range(-a,a+1):
    s = s + ' ' + str(i)
print(s)

"""
"""
Напишите программуб которая будет принимать на вход 
дробь и показывать первую цифру дробной части числа.
_____________________________________________________

text = str(input('Input your digit: '))
#print(len(text))
if len(text) < 5 and len(text) > 1:
    print(text[2])    
else:
    print('No')
"""

"""Напишите программу которая принимает на вход число
    и проверяет кратно ли оно 10 или 15, но не 30.

a = int(input('Input your digit: '))
result = (a%10 == 0 or a%15 == 0) and a%30 != 0:
print(result)
"""
