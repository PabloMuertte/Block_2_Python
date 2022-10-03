"""
Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



def uneven_sum_result (list_1):
    uneven_sum = 0
    for i in range (0,len(list_1)):
        if i%2 != 0:
            uneven_sum+=list_1[i]
    return uneven_sum

list_1 = [2,3,5,9,3]
print(uneven_sum_result(list_1))
"""

"""
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

"""

def pair_sum_1 (list_1):
    if len(list_1)%2==0:
        even_list = True
        s=[]
        if even_list == True: 
            for i in range(0,int(len(list_1)/2)):
                n=len(list_1)-i
                first = list_1[i]
                last = list_1[n-1]
                first_multi_last=first*last
                s.append(first_multi_last)
        return s
    else:
        even_list = False
        if even_list == False:
            s=[]
            for i in range(0,int(len(list_1)/2)):
                n=len(list_1)-i
                first = list_1[i]
                last = list_1[n-1]
                multiplied=first*last
                s.append(multiplied)
            middle_digit = 2**int(((len(list_1)-1)/2)**2)
            s.append(middle_digit)
        return s

#list_1 = [2, 3, 5, 6]
list_1 = [2, 3, 4, 5, 6]
print(pair_sum_1(list_1))

