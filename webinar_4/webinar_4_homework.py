""" 
Task 1
Вычислить число c заданной точностью d
Пример:
при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d =  int(input("Введите число для заданной точности числа Пи: "))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
"""


"""
Task 2
Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N.
 
n = int(input("Введите число: "))
i = 2 
lst = []
num_1 = n
while i <= n:
    if n % i == 0:
        lst.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {num_1} приведены в списке: {lst}") 
"""
"""
Task 3
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

a = [1,2,2,2,2,3,1,4]
print(set (a))
"""

"""
Task 4
Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
""" # честно сам не решал нашел в интернете
from random import randint

print('Чтобы сформировать многочлен степени k и записать в файл, введите степень k! ')
k = int(input("Введите степень k: "))

factor = []
for i in range(1, k +2):
    factor.append(randint(1, 101))

result = []
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}')
    signs =randint(0,1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)
result.append('=0')

record = open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_4/data.txt', 'w')
record.write(''.join(result))
record.close() 
 """

""" 
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
 """

ffile1 = open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_4/data_1.txt', 'r')
ffile2 = open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_4/data_2.txt', 'r')
ffile3 = open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_4/data_3.txt', 'w')
file1 = ffile1.readline()
file2 = ffile2.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            ffile3.write(str(int(file1[i])+int(file2[i])))
        else:
            ffile3.write(str(file1[i]))
    else:
        ffile3.write(str(file1[i]))
ffile1.close
ffile2.close
ffile3.close

