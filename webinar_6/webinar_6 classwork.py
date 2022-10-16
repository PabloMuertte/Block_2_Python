""" Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. Приоритет операций стандартный.
Пример:
2+2 => 4
1+2*3 => 7
1-2*3 => -5
Добавте возможность использования скобок, меняющих приоритет операций.
Пример:
(1+2)*3 => 9
 """




input_list= input("Введите выражение: ").split()
output = []
stack_list = []
for element in input_list:
    if element.isdigit():
        output.append(element)
    elif element == "(":
        stack_list.append(element)
    elif element == ")":
        while stack_list and stack_list[-1]!= "(":
            output.append(stack_list.pop()) #забираем последний элемент из стек и помещаем в аутпут
        if not stack_list:
            print("несогласованные скобки") 
            exit()
        stack_list.pop()
    elif element in ["*","/"]:
        while stack_list and stack_list[-1] in ["*","/"]:
            output.append(stack_list.pop())
        stack_list.append(element)
    elif element in ["+","-"]:
        while stack_list and stack_list[-1] in ["*","/","+","-"]:
            output.append(stack_list.pop())
        stack_list.append(element)
    else:
        print("Нераспознаный знак")
        exit()
while stack_list:
    if stack_list[-1] not in ["*","/","+","-"]:
        print("Несогалсованны скобки")
        exit()
    output.append(stack_list.pop())
print(output)

result = []
for element in output:
    if element.isdigit():
        result.append(int(element))
    else:
        b = result.pop()
        a = result.pop()
        if element == "+":
            result.append(a+b)
        elif element == "-":
            result.append(a-b)
        elif element == "*":
            result.append(a*b)
        elif element == "/":
            result.append(a/b)
print(result[0])


