"""
В файле хранятся числа, нужно выбрать четные и составить
список пар (число; квадрат числа)
пример-
1 2 3 5 8 15 23 38
результат
[(2,4),(8,64)(38,1444)]
#file_sim_3.write(str('1 2 3 5 8 15 23 38'))
"""
from curses.ascii import isdigit


""" def square (s):
    return s**2

file_sim_3 = open('/home/pablo/Documents/Python GB/Block_2_Python/siminar_1_2_3/data_sim_3.txt', 'r')
file1 = file_sim_3.readline()
list=file1.split()
list_2 = [(int(list[i]),square(int(list[i]))) for i in range (1,len(list)) if int(list[i])%2==0]
print(list_2) """

def select (f,col):
    return [f(x) for x in col]

def where (f,col):
    return [x for x in col if f(x)]

data = open('/home/pablo/Documents/Python GB/Block_2_Python/siminar_1_2_3/data_sim_3.txt', 'r')
list_data = data.readline().split()
res = select(int,list_data)
res = where(lambda x: not x%2, res)
res = select(lambda x: (x,x**2), res)
print(res)

  
