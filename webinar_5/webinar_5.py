"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#От себя добавил чтение и запись в файл.
"""
""" 
data = open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_5/webinar_5_task_1.txt','r')
txt_1=data.readline()
print(txt_1)
list_1 = txt_1.split(' ')
fragment = 'абв'
new_list = []
for word in list_1:
    if fragment not in word:
        new_list.append(word)
new_txt=' '.join(new_list)
print(new_txt)

with open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_5/webinar_5_task_1_result.txt', 'w') as data1:
    data1.writelines(new_txt) 
"""

"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""
""" 
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}") 
    """

"""
    Создайте программу для игры в ""Крестики-нолики"".
"""
""" 
def print_m(matrix_new):
    for i in matrix_new: 
        for i2 in i: 
            print(i2, end=' ') 
        print()

def find_item_X (matrix,x):
    for i in range (0,3):
        for j in range (0,3):
            if matrix[i][j] == x:
                matrix[i][j] = str('X')
    return matrix

def find_item_O (matrix,x):
    for i in range (0,3):
        for j in range (0,3):
            if matrix[i][j] == x:
                matrix[i][j] = str('O')
    return matrix

def winer_check(matrix_2,c):
    if matrix_1[0][0]==matrix_1[0][1]==matrix_1[0][2]:
        if c==1:
            winer = 'Player_1'
            print('And our winer',winer)
            exit()
        elif c==2:
            winer = 'Player_2'
            print('And our winer',winer)
            exit()
    elif matrix_1[1][0]==matrix_1[1][1]==matrix_1[1][2]:
        if c==1:
            winer = 'Player_1'
            print('And our winer',winer)
            exit()
        elif c==2:
            winer = 'Player_2'
            print('And our winer',winer)
            exit()
    elif matrix_1[2][0]==matrix_1[2][1]==matrix_1[2][2]:
        if c==1:
            winer = 'Player_1'
            print('And our winer',winer)
            exit()
        elif c==2:
            winer = 'Player_2'
            print('And our winer',winer)
            exit()
    elif matrix_1[0][0]==matrix_1[1][0]==matrix_1[2][0]:
        if c==1:
            winer = 'Player_1'
            print('And our winer',winer)
            exit()
        elif c==2:
            winer = 'Player_2'
            print('And our winer',winer)
            exit()
    elif matrix_1[0][1]==matrix_1[1][1]==matrix_1[2][1]:
        if c==1:
            winer = 'Player_1'
            print('And our winer',winer)
            exit()
        elif c==2:
            winer = 'Player_2'
            print('And our winer',winer)
            exit()
    elif matrix_1[0][2]==matrix_1[1][2]==matrix_1[2][2]:
        if c==1:
            winer = 'Player_1'
            print('And our winer',winer)
            exit()
        elif c==2:
            winer = 'Player_2'
            print('And our winer',winer)
            exit()
    elif matrix_1[0][0]==matrix_1[1][1]==matrix_1[2][2]:
        if c==1:
            winer = 'Player_1'
            print('And our winer',winer)
            exit()
        elif c==2:
            winer = 'Player_2'
            print('And our winer',winer)
            exit()
    elif matrix_1[2][0]==matrix_1[1][1]==matrix_1[0][2]:
        if c==1:
            winer = 'Player_1'
            print('And our winer',winer)
            exit()
        elif c==2:
            winer = 'Player_2'
            print('And our winer',winer)
            exit() 

def game (matrix_1):
    for i in range (0,9):
        if i<=9:
            c = 1
            X =int(input('Player 1, Please insert number for you X! '))
            print()
            matrix = find_item_X(matrix_1,X)
            print_m(matrix)
            winer_check(matrix,c)
            c=2
            O =int(input('Player 2, Please insert number for you O! '))
            print()
            matrix = find_item_O(matrix,O)
            print_m(matrix)
            winer_check(matrix,c)      

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Lets play tick-tack-toe!')
print()
print_m(matrix_1)
print()
game(matrix_1) 
"""


"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Кодирование длин серий (англ. run-length encoding, RLE) или кодирование повторов — 
алгоритм сжатия данных, заменяющий повторяющиеся символы (серии) на один символ и число его повторов. 
Серией называется последовательность, состоящая из нескольких одинаковых символов.

Входные и выходные данные хранятся в отдельных текстовых файлах.
"""

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char !=prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count+= 1
    else:
        encoding+= str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count= ''
    for char in data:
        if char.isdigit():
            count+= char
        else:
            decode += char * int(count)
            count = ''
    return decode

data = open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_5/webinar_5_task_5.txt','r')
txt_1=data.readline()
print('Original text: ',txt_1)
encoded_val = rle_encode(txt_1)
print('Encoded text: ',encoded_val)
with open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_5/webinar_5_task_5_encoded_result.txt', 'w') as data1:
    data1.writelines(encoded_val)

decoded_val = rle_decode(encoded_val)
print('Decoded text: ',decoded_val)
with open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_5/webinar_5_task_5_decoded_result.txt', 'w') as data1:
    data1.writelines(decoded_val)



