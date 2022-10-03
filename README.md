# Block_2_Python

Commands
print (type(a)) - print type of variable
print(f) - print variable
a = int(input('text')) вывод текста и присвоение введенных данных переменной


text = 'text ..... text'
print(len(text))  #количество символов
print('text' in text ) # True // наличие набора символов в переменной строка
print(text.isdigit()) #False // проверка на заполнение цифрами
print(text.islower()) #True //проверка региста
print(text.replace('text','TEXT')) # замена набора символов на другой набор символов
print(text[2]) # рассмотрение текста как массива и вывод введенного элемента массива


colors = ['red','green','blue']
data = open('file.txt','a')
data.writelines(colors) #разделителей не будет
data.close()

exit()
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

Как работать с файлами:
Связать файловую переменную с файлом,
определив модификатор работы
a – открытие для добавления данных
r – открытие для чтения данных
w – открытие для записи данных
w+, r+

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()