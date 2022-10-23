from phone_contacts_extractor import write_contact
from phone_contacts_extractor import search_phone_book

def new_contact():
    new_data = input("Insert Contact information by space,\nLast name, First name, Phone number, Discription: ").split()
    write_contact(new_data)


def search_contact():
    search_data = str(input("Insert part of contact that you search: "))
    search_phone_book(search_data)