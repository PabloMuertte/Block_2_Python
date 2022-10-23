from calculations import calculation
from logger import read_log

def main_menu ():
    flag = True
    while flag:
        print("Hello, launched Calculator programm")
        while True:
            print("1 - To make calculation")
            print("2 - Show log file")
            print("3 - to Exit")
            choice = input()
            if choice not in ["1","2","3",]:
                print("Incorrect input, try again!")
                continue
            if choice == "1":
                calculation()
                break
            elif choice == "2":
                read_log()
                break
            else:
                flag = False
                break


if __name__ == "__main__":
    main_menu()