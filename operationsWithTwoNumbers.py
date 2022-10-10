from unittest import result


print("Calculator of two numbers")

n1 = input("Type the first number: ")
try:
    n1 = int(n1)
except:
    n1 = "badTyping"
    
if n1 == "badTyping":
    print("Please just put integer numbers the next time")
    exit()

n2 = input("Type the second number: ")
try:
    n2 = int(n2)
except:
    n2 = "badTyping"
    
if n2 == "badTyping":
    print("Please just put integer numbers the next time")
    exit()
    
operator = input("Type the operator '+', '-', '*', '/': ")

if operator == "+":
    result = n1 + n2
    print("The result of adding " + str(n1) + " + " + str(n2) + " is = " + str(result))
elif operator == "-":
    result = n1 - n2
    print("The result of substracting " + str(n1) + " + " + str(n2) + " is = " + str(result))
elif operator == "*":
    result = n1 * n2
    print("The result of multiplying " + str(n1) + " + " + str(n2) + " is = " + str(result))
elif operator == "/":
    result = n1 / n2
    print("The result of dividing " + str(n1) + " + " + str(n2) + " is = " + str(result))
else:
    print("You didn't type a correct operator symbol")