from operations import create_employer
from operations import search_employer
from operations import edit_search_employer
from operations import delete_employer
from operations import add_new_data

def new_employer():
    new_data = input("\nInsert Employer information by space,\nLast name, First name, Phone number, Title, Salary: \n").split()
    create_employer(new_data)


def search_contact():
    search_data = str(input("\nInsert contact details of Employer that you want search: "))
    search_employer(search_data)

def edit_employer():
    search_data = str(input("\nInsert contact details of Employer which you want to search and edit: "))
    search_employer(search_data)
    edit_data = int(input("\nPress-1 To edit First Name \nPress-2 To edit Last Name\nPress-3 To edit Phone number\nPress-4 To edit Title\nPress-5 To Edit Salary\nPress-0 To Exit\n:"))
    if edit_data !=0:
        new_data = input("insert new infornation  :")
        edit_search_employer(search_data,edit_data,new_data)


def del_employer():
    data = str(input("\nInsert contact details of Employer that you want search and delete: \n"))
    delete_employer(data)


def add_data():
    search_data = input("\nInsert contact details of Employer which you want to search and add new data: ")
    search_employer(search_data)
    new_data = input('Insert information to add to Employer: ')
    add_new_data(search_data,new_data)

