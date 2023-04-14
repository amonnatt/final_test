def chack_car (number):
    van=0
    car=0
    while number>0:
        if number >4:
            number -=11
            van +=1
        elif number>0 and number <=4: 
            car += 1
            number -=4      
        else:
            break   
    return ("van: %d"%van)+" "+("car: %d"%car)

def validate_number(number):
    if type(number) != int:
        if type(number) == str:
            return "input integer"
        elif number >= 0:
            return "input integer"
        else:
            return "out of range"
    elif number >= 1:
        return number
    else:
        return "out of range"

def display(number):
    result = validate_number(number)
    if type(result) == int:
        return chack_car(result)
    else:
        return result
    