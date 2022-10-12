def function():
    print("I'm in a function")

def functionArgument(argument):
    print("Function with argument: " + argument)

def functionNames(name, lastname):
    print("Hello, my name is: " + name + " and my lastname is: " + lastname)

def otherFunction(*products):
    print("The supermarket list: ", products)

def functionKeywordArgs(**kwdargs):
    print("KeywordArgs, my name is: " + kwdargs["name"] + " and my lastname is: " + kwdargs["lastname"])

def functionStaticArgument(argument = "Table"):
    print(argument)

def functionWithLists(products):
    index = 1
    for product in products:
        print("Item: " + str(index) + " - Product: " + product)
        index += 1

def functionConcatAndReturn(products):
    temp = ''
    for product in products:
        temp += product + ' '
    return temp

function()
functionArgument("Argument from the calling")
functionNames("Harvey","Specter")
functionNames(lastname="Bond", name="James")
otherFunction("Milk", "Fruit", "Vegetables", "Soap", "Break", "Salt", "Sugar")
functionKeywordArgs(name="MYNAME", lastname="MYLASTNAME")
functionStaticArgument()
functionStaticArgument("Chair")
functionWithLists(["Milk", "Fruit", "Vegetables", "Soap", "Break", "Salt", "Sugar"])
products = functionConcatAndReturn(["Leon", "Perez"])
print(products)