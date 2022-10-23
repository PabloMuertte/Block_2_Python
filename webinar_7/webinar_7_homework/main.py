from phone_contacts_extractor import read_phone_book
from input import search_contact
from input import new_contact
from json_extractor import json_extract

def main_menu ():
    flag = True
    while flag:
        print("Hello, you launched Telephone book programm")
        while True:
            print("Press-1 To insert new telephone contact")
            print("Press-2 To Show telephone book")
            print("Press-3 To search contact")
            print("Press-4 To export phone book")
            print("Press-5 to Exit")
            choice = input()
            if choice not in ["1","2","3","4","5"]:
                print("Incorrect input, try again!")
                continue
            if choice == "1":
                new_contact()
                break
            elif choice == "2":
                read_phone_book()
                break
            elif choice == "3":
                search_contact()
                break
            elif choice == "4":
                json_extract()
                break
            else:
                flag = False
                break


if __name__ == "__main__":
    main_menu()