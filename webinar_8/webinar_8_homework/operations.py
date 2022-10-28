from random import randint

FILE_NAME = "/home/pablo/Documents/Python GB/Block_2_Python/webinar_8/webinar_8_homework/employers_database.csv"

def check_id_gen_new():
    n = randint(1,999)
    with open(FILE_NAME, 'r', encoding= "UTF-8") as f:
        for line in enumerate(f,1):
            if n not in line:
                return n
            else:
                return check_id_gen_new()


def create_employer(new_data):
    n= check_id_gen_new()  
    with open(FILE_NAME, 'a', encoding= "UTF-8") as f:
        f.writelines(f"\n{n}, {new_data[0]}, {new_data[1]}, {new_data[2]}, {new_data[3]}, {new_data[4]},")
        

def read_list_employers():
    with open (FILE_NAME, "r",encoding="UTF-8") as f:
        print("List of Employers\n")
        print(f.read())
        print()       


def search_employer(search):
    with open (FILE_NAME, "r",encoding="UTF-8") as f:   
        lines = f.readlines()
        for line in lines:
            if line.find(search) != -1:
                print('Result of search: ', line)
                print()
                return line
            

def edit_search_employer(search,data,new):
    with open (FILE_NAME, "r",encoding="UTF-8") as f: 
        for num, line in enumerate(f,1):
            if search in line:
                list_line = list(line.split(" "))              
                list_line[data] = new + ','
                new_str = ' '.join(list_line)
                print(new_str)
                with open (FILE_NAME, "r",encoding="UTF-8") as f:   
                    lines = f.readlines()
                    lines[num-1] = new_str
                    with open (FILE_NAME, "w",encoding="UTF-8") as f:
                        f.writelines(lines)


def delete_employer(data):
    search = search_employer(data)
    print(f'\nAttention!\n{search}Will be deleted!')
    confirm = input('Input y/n to confirm or no to cancel:  ')
    if confirm == 'y':
        with open (FILE_NAME, "r",encoding="UTF-8") as f:
            for num, line in enumerate(f,1):
                if search in line:
                    with open (FILE_NAME, "r",encoding="UTF-8") as f:   
                        lines = f.readlines()
                        lines[num-1] = ''
                        with open (FILE_NAME, "w",encoding="UTF-8") as f:
                            f.writelines(lines)
    elif confirm == 'n':
        exit


def add_new_data(search,new_data):
    with open (FILE_NAME, "r",encoding="UTF-8") as f: 
        for num, line in enumerate(f,1):
            if search in line:
                print(num)
                print(len(line))
                line =  line[0:37]+','
                list_line = list(line.split(" "))
                print(list_line)              
                list_line.append(new_data)
                print(list_line)
                new_str = ' '.join(list_line)
                new_str = new_str + '\n'
                with open (FILE_NAME, "r",encoding="UTF-8") as f:   
                    lines = f.readlines()
                    lines[num-1] = new_str
                    with open (FILE_NAME, "w",encoding="UTF-8") as f:
                        f.writelines(lines)



