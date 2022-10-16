"""
1. В файле находится N Натуральных чисел, записанных через пробел.
Среди чисел не хватает одного числа, чтобы выполнялось условие A[i]-1=A[i-1]. Найдите это число.


def readfile_writeto_list (txtfile):
    with open(str(txtfile), 'r' ) as data:
        numbers=data.read()
    return [int(i) for i in numbers.split()]

file_1 = '/home/pablo/Documents/Python GB/Block_2_Python/webinar_5/textfile_classwork_1.txt'
temp_result= readfile_writeto_list(file_1)
print(temp_result)
for i in range(1, len(temp_result)):
    if temp_result[i-1] != temp_result[i]-1:
        print(temp_result[i-1]+1)

 """



"""
2. Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
Порядок элементов менять нельзя.
Пример:
[1,5,2,3,4,6,1,7] => [1,2,3] или [1,7] or [1,6,7]

"""