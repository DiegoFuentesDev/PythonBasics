dictionaryNames = {
    "name" : "John Smith",
    "age" : 25,
    "occupation" : "Lawyer",
    "hobbie" : "Cinema",
    "Game Console" : "Xbox"
}

print("Dictionary:",dictionaryNames)
print("Only the name",dictionaryNames["name"])
dictionaryNames["name"] = "Kevin Potter"
print("Name Changed:",dictionaryNames)
print("Number of elements in the dictionary:",len(dictionaryNames))
dictionaryNames["Gender"] = "Male"
dictionaryNames.pop("age")
print("The dictionary after pop the element 'age'",dictionaryNames)
dictionaryNames.popitem()
print("The dictionary after use the .popitem in the dictionary, that remove the last element of it:", dictionaryNames)
dictionaryCopy = dictionaryNames.copy()
dictionaryDelete = dict(dictionaryCopy)
dictionaryDelete.clear()
print("Original", dictionaryNames)
print("Copy", dictionaryCopy)
print("Deleted", dictionaryDelete)