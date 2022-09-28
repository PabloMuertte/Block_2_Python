"""
Напишите программу, которая принимает на вход вещественное 
число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11


def sum_digits_string(str1):
    sum_digit = 0
    for i in str1:
        if i.isdigit() == True:
            z = int(i)
            sum_digit = sum_digit + z

    return sum_digit

str1 = str(input('Please insert your digit to calculating: '))
print(sum_digits_string(str1))


Напишите программу, которая принимает на вход число N и 
выдает набор произведений чисел от 1 до N.
Пример:
 пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Please insert your number :'))
j_sum = 1
list1 =[]
for i in range (1, n+1):
    j_sum = i*j_sum
    list1.append(str(j_sum))
print('[',', '.join(list1),']')





Задайте список из n чисел последовательности (1+1/n)**n 
и выведите на экран их сумму.

Пример:

n = int(input('Please insert your number :'))
j_sum = 0
list1 =[]
for i in range (1, n+1):
    j_sum = round((1+1/i)**i,2)
    list1.append(str(j_sum))
print('{',', '.join(list1),'}')


n = int(input ('Please input your number: '))
d = dict() # d= {}
j = 1
for i in range(1,n+1):
    r = round((1+1/i)**i,2)
    d[j] = r
    j+=1
print(d)
"""
"""
Реализуйте алгоритм перемешивания списка.

from random import sample

str_1 = ['Ананас','Яблоко','Вишня','Виноград','Томат']
str_2 = sample(str_1, k=5)
print(str_2)
"""
    
str_1 = ['Ананас','Яблоко','Вишня','Виноград','Томат']

