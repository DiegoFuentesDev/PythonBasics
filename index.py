lista = [1, 2 , 3, 4] #array
print("lista",lista)
lista2 = lista.copy() #cloning the array in other variable
print("lista2 = lista.copy()",lista2)
lista.append(2) #adding an element
print("lista.append(2)",lista)
lista.clear() #delete all the elements in the array
print("lista.clear()",lista)
lista2.append(2)
print("lista2.append(2)",lista2)
print("lista2.count(2) = ",lista2.count(2)) # print how many specific repeated elements there are
print("len(lista2)",len(lista2),"elementos en el arreglo") # print how many elements are
print("1er elemento del arreglo =",lista2[0]) # print the first element in the array
print("2do elemento del arreglo =",lista2[1]) # print the second
print("3er elemento del arreglo =",lista2[3]) # print the third
listaNombres = ["John", "Arthur", "Henry", "Alex", "Liam"]
print("listaNombres",listaNombres)
print("listaNombres.pop()",listaNombres.pop()) # print the deleted element (the last one)
print("listaNombres despues de .pop()",listaNombres)
print("listaNombres.remove('Arthur')",listaNombres.remove("Arthur")) # removing an specific element from the array
print("listaNombres",listaNombres)
