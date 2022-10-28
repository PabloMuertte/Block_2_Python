from input import new_employer
from operations import read_list_employers
from input import search_contact
from input import edit_employer
from input import del_employer
from input import add_data

def main_menu ():
    flag = True
    while flag:
        print("Hello, you launched CRM programm\n")
        
        while True:
            print("Press-1 To create new employer")
            print("Press-2 To Show all employers")
            print("Press-3 To search employer")
            print("Press-4 To edit employer data")
            print("Press-5 To add Employer data")
            print("Press-6 To delete employer")
            print("Press-7 to Exit")
            print()
            choice = input()
            if choice not in ["1","2","3","4","5","6","7"]:
                print("Incorrect input, try again!")
                continue
            if choice == "1":
                new_employer()
                break
            elif choice == "2":
                read_list_employers()
                break
            elif choice == "3":
                search_contact()
                break
            elif choice == "4":
                edit_employer()
                break
            elif choice == "5":
                add_data()
                break
            elif choice == "6":
                del_employer()
                break
            else:
                flag = False
                break


if __name__ == "__main__":
    main_menu()