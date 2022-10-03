"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.



from unittest import result


positions = []
with open ('/home/pablo/Documents/Python GB/Block_2_Python/Webinar_3/file1.txt','r', encoding='utf-8') as f:
    positions = f.read().split()
    positions = [int(i) for i in positions]
n = int(input('Insert full digit: '))
s = []
for i in range(-n, n + 1):
    s.append(i)
result = 1
for i in range(len(positions)):
    result *= s[positions[i] - 1]
print(f'Your List: {s}.\nYour Posittions: {positions}.')
print(result)
"""

"""
1.Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

2.Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет.
*Пример*
- список:["qwe", "asd", "zxc", "qwe", "ertqwe"],ищем:"qwe", result:3
- список:["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список:["йцу", "фыв", "ячс", "цук", "йцукен"], ищем "йцу", ответ: -1
- список:["123", "234", 123, "567"], ищем: "123", ответ -1
- список:[],ищем "123", ответ: -1


def list_search (my_full_list,f):
    for i in range(0,len(my_full_list)):
        for j in range(0,len(my_full_list[i])) :
            if my_full_list[i][j] == f:
                print(f'Your text finded: String number {i+1}, Position number {j+1}')
                continue

my_list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
my_list_2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
my_list_3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
my_list_4 = ["123", "234", 123, "567"]
my_list_5 = []
my_full_list = [my_list_1,my_list_2,my_list_3,my_list_4,my_list_5]

#print(my_full_list)
print(f'Your lists: \n{my_list_1},\n{my_list_2},\n{my_list_3},\n{my_list_4},\n{my_list_5}')
f = str(input('Insert your text search: '))
print(list_search(my_full_list,f))
"""

""" 

def list_search (my_full_list,f):
    count = 0
    for i in range(0,len(my_full_list)):
        for j in range(0,len(my_full_list[i])) :
            if my_full_list[i][j] == f:
                count+= +1               
                if count == 2:
                    print(f'Your text second find: String number {i+1}, Position number {j+1}')      
                if count==1 and count !=2:
                    print(-1)  
                

my_list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
my_list_2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
my_list_3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
my_list_4 = ["123", "234", 123, "567"]
my_list_5 = []
my_full_list = [my_list_1,my_list_2,my_list_3,my_list_4,my_list_5]

#print(my_full_list)
print(f'Your lists: \n{my_list_1},\n{my_list_2},\n{my_list_3},\n{my_list_4},\n{my_list_5}')
f = str(input('Insert your text search: '))
print(list_search(my_full_list,f))
         """

"""
Реализуйте алгоритм задания случайных чисел 
без использования встроенного генератора псевдослучайных чисел.



import time

now = time.time()
#print(now)
print(str(now).split('.')[1][0])
"""