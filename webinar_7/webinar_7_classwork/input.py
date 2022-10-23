def input_number():
    while True:
        a = input("Insert number: ")
        try:
            return float(a)
        except:
            try: 
                x = float(a.strip("j"))
                while True:
                    y = input("Input real part of complex number: ")
                    try:
                        return complex(float(y),x)
                    except:
                        print("Incorrect input, please try again!")
            except:
                print("Incorrect input, try again!")
            

def input_operation():
    while True:
        print("Insert number of operation: ")
        print("1 - Summary")
        print("2 - Subtraction")
        print("3 - Multiply")
        print("4 - Division")
        # print("0 - Return to main menu")
        op = input()
        if op not in ["1","2","3","4"]:
            print ("Incorrect input, try again!")
            continue
        return op
