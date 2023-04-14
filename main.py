from function import display

c = "y"
while c == "y":
    input_number = input("Number : ")
    try:
        try:
            input_number = int(input_number)
        except:
            input_number = float(input_number)
    except:
        input_number = str(input_number)

    result = display(input_number)
    print(result)
    c = input("(y/n) :")