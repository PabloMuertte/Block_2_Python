"""
Task 1
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
Task 2
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]



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
                s.append(list_1[i] * list_1[n-1])
            middle_digit = 2**int(((len(list_1)-1)/2)**2)
            s.append(middle_digit)
        return s

#list_1 = [2, 3, 5, 6]
list_1 = [2, 3, 4, 5, 6]
print(pair_sum_1(list_1))
"""

"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.
Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def dig_after_point (list_1):
    s=[]
    for i in range (0,len(list_1)):
        m=list_1[i]*100
        m= m%100
        if m==0:
            m=1
        s.append(int(m))
    return s

def dif_min_max (list_2):
    
    for i in range(0,len(list_2)):
        min_1 = list_2[1]
        max_1 = list_2[1]
        #print(list_2[i])
        if list_2[i] > max_1:
            max_1 = list_2[i]
        elif list_2[i]< min_1:
            min_1 = list_2[i]
    return (max_1-min_1)/100           
   
list_1 = [1.1, 1.2, 3.1, 5, 10.01]
list_2=dig_after_point(list_1)
print(dif_min_max(list_2))
"""

"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 

n = int(input('Please insert your number for Conversion to decimal : '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2

print('Your decimal number is',b,'.')
"""



""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Enter any number: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)
"""
""" def fibonachi (n):
    if n in [1,2]:
        return 1
    else:
        return fibonachi (n-1) + fibonachi(n-2)

def nega_fibonachi (n):
    list_negafibonachi = [0]
    for i in range (1,n + 1):
        list_negafibonachi.append(fibonachi(i))
        list_negafibonachi.insert(0, (fibonachi(i) * (-1)**(i+1)))
    return list_negafibonachi

n = int(input('Insert your number to get list negafibonachi: '))
print(f"Your list of negafibonachi numbers for inserted number {n} is: {nega_fibonachi(n)}") """