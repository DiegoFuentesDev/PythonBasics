print("Tuples")
tuple = ("Hello","World","From","Tuples")
print("Original Tuple",tuple)
print("tuple.count('Hello')",tuple.count("Hello"))
print("tuple.index('From')",tuple.index("From"))
print("tuple.append('GG'), it will be a mistake because tuple object has not attribute append")
print("If we want to do this we have to Cast the tuple to a list")
listFromTuple = list(tuple)
print("And this will be our list from a tuple = ",listFromTuple)
print("As you can see, it has brackets, not parenthesis")
listFromTuple.append("GG")
print("And now we can add 'GG' at the end of the object",listFromTuple)
