"""
Task 1
Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет

print('Please input your number of the day from 1 to 7 :')
a = int(input())
if a == (6 or 7):
    print('This is the weekend!')
else:
    a == range(6)
    print('This is work day!')
"""

"""
Task 2
Напишите программу для. проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def logical_statement(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")
"""    
    
"""
Task 3 
Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3


x = int(input('Input X coordinate :'))
y = int(input('Input Y coordinate :'))

if (x == 0 or y==0):
    print('Coordinates must be above zero!')
    exit()
if(x>0 and y>0): 
    result = 1
elif(x<0 and y>0):
    result = 2
elif(x<0 and y<0): 
    result = 3
elif(x>0 and y<0): 
    result = 4
print('Quater of your coordinates is',result, '.')
"""

"""
Task 4
Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).


quater = int(input('Please input quater of X*Y coordinates :'))

if (quater == 1):
    print('Range of your coordinates: x > 0 and y > 0')
elif (quater == 2):
    print('Range of your coordinates: x < 0 and y > 0')
elif (quater == 3):
    print('Range of your coordinates: x < 0 and y < 0')
elif (quater == 4):
    print('Range of your coordinates: x > 0 and y < 0')
"""

"""
Напишите программу, которая принимает на вход координаты двух точек и 
находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21

    Math.Sqrt((y_2-y_1)*(y_2-y_1)+(x_2-x_1)*(x_2-x_1));
    Distance(x_1,x_2,y_1,y_2);


import math


def Distance(x_1,x_2,y_1,y_2):
    distance = math.sqrt ((y_2-y_1)*(y_2-y_1)+(x_2-x_1)*(x_2-x_1))
    return distance

x_1 = int(input('X coordinate of point A : '))
y_1 = int(input('Y coordinate of point A : '))
x_2 = int(input('X coordinate of point B : '))
y_2 = int(input('Y coordinate of point B : '))

txtDistance = str(Distance(x_1,x_2,y_1,y_2))
print('Distance bitween coordinates is',txtDistance[0:4], '.')
"""