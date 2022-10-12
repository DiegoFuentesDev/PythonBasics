def recursivity(number):
    if(number < 1):
        return number
    print(number, end=", ")
    recursivity(number - 1)

recursivity(10)