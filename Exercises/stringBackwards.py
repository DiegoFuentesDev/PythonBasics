name = str(input('Type your name: '))
surname = str(input('Type your surname: '))

#using str functions
print(name[::-1])
print(surname[::-1])


#using lsit to better manage of them
listName = []
listSurname = []

for i in name:
    listName.append(i)
listName.reverse()

for i in surname:
    listSurname.append(i)
listSurname.reverse()

print('Name backward:')
for i in listName:
    print(i,end='')

print('\nSurname backward:')
for i in listSurname:
    print(i,end='')