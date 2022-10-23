
FILE_NAME = "/home/pablo/Documents/Python GB/Block_2_Python/webinar_7/webinar_7_homework/phone_book.csv"

def write_contact(new_data):
    with open(FILE_NAME, 'a', encoding= "UTF-8") as f:
         f.writelines(f"\n{new_data[0]}, {new_data[1]}, {new_data[2]}, {new_data[3]}")


def read_phone_book():
    with open (FILE_NAME, "r",encoding="UTF-8") as f:
        print(f.read())


def search_phone_book(search):
    with open (FILE_NAME, "r",encoding="UTF-8") as f:   
        lines = f.readlines()
        for line in lines:
            if line.find(search) != -1:
                print('Result of search: ', line)
                

