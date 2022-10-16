"""
#1
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
Использование list comprehension

data = open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_6/webinar_6_task_1.txt','r')
txt_1=data.readline()
print("Исходный текст: ", txt_1)
list_1 = txt_1.split(' ')
fragment = 'абв'
new_list = [ word for word in list_1 if not "абв" in word]     
new_txt=' '.join(new_list)
print("Обработанный текс:", new_txt)
with open('/home/pablo/Documents/Python GB/Block_2_Python/webinar_6/webinar_6_task_1_result.txt', 'w') as data1:
    data1.writelines(new_txt)
""" 

""" 
#2
Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
 
input_list = input("Insert list of digits, split by space: ").split()
print(sum([int(input_list[i]) for i in range(1,len(input_list),2) if input_list[i].isdigit()]))
"""

"""
#3
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] 


def list_lenght(my_list):
    if len(my_list) % 2 == 0:
        lenght = len(my_list) // 2
    else:
        lenght = len(my_list) //2 + 1
    return lenght

input_list = list(map(int, input("Input list of digits, split by space: ").split()))
new_list = [(input_list[i])* (input_list[len(input_list)-1-i]) for i in range(list_lenght(input_list))]
print(input_list,new_list)
"""
 

"""
#4
Напишите программу, которая принимает на вход вещественное 
число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11


input = input("Input your number: ")
sum_new = sum([int(digit) for digit in input if digit.isdigit()])
print(sum_new)
"""

"""
#5
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.
Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list_1 = [1.1, 1.2, 3.1, 5, 10.01]
fract_list = [round(i % 1,2) for i in list_1 if i%1 != 0]
print("For list:",list_1," difference between Max and Min fractional part is ",(max(fract_list)- min(fract_list)))
"""