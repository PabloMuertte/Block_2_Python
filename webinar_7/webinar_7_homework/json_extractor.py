import json

def json_extract():
    filename = '/home/pablo/Documents/Python GB/Block_2_Python/webinar_7/webinar_7_homework/phone_book.csv'
    dict1 = {}
    fields =['Last_name', 'First_name', 'Phone_number', 'discription']

    with open(filename) as fh:
        l = 1
        for line in fh:
            description = list( line.strip().split(None, 4))
            print(description)
            sno ='Contact'+str(l)
            i = 0
            dict2 = {}
            while i<len(fields):                   
                    dict2[fields[i]]= description[i]
                    i = i + 1
            dict1[sno]= dict2
            l = l + 1	
    out_file = open("/home/pablo/Documents/Python GB/Block_2_Python/webinar_7/webinar_7_homework/phone_book.json", "w")
    json.dump(dict1, out_file, indent = 4)
    out_file.close()

