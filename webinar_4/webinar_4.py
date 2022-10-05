"""
Задайте строку из набора чисел. Напишите программу, 
которая покажет большее и меньшее число. 
В качестве символа-разделителя используйте пробел.

from random import randint

def random_list (N):
    s=[]
    for i in range (0,N):
        n_1 = randint(0, 10)
        s.append(n_1)
    return s

def list_to_str (list):
    s = ''
    for i in range(0,len(list)):
        s+= str(list[i])+' '
    return s

print('This program create string with random numbers and show \nMinimal and Maximal digits of this string.')
n = int(input('Please insert number of elements:  '))
rand_list =random_list(n)
str_n = list_to_str(rand_list)
print()
print('Your string with random digits: ',str_n)
print(type(str_n))
print('Minimal digit is:',min(rand_list),'\nMaximal digit is:',max(rand_list))
"""

"""
Найдите корни квадратного уравнения ax^2 + bx + c = 0
1. с помощью математических формул нахождения корней квадратного уравнения;
2. с помощью дополнительных библиотек Python (numpy.roots)
"""

import numpy as np

p= [1,5,6]
roots = np.roots(p)
print(roots)