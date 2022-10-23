from datetime import datetime

FILE_NAME = "/home/pablo/Documents/Python GB/Block_2_Python/webinar_7/webinar_7_classwork/calc_log.csv"

def write_log(num1,num2,operation,result):
    with open(FILE_NAME, 'a', encoding= "UTF-8") as f:
         f.writelines(f"\n{datetime.now().strftime('%d.%m.%Y %H:%M')} Inserted digits: {num1},{num2}. Operation {operation}. Result {result}.\n")


def read_log():
    with open (FILE_NAME, "r",encoding="UTF-8") as f:
        print(f.read())

