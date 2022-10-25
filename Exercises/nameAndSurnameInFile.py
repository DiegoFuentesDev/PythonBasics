def nameAndSurname(name,surname):
    theFile = open('names.txt', 'a')
    theFile.write(name + ' ' + surname + '\n')
    theFile.close()

name = input('Enter your name: ')
surname = input('Enter your surname: ')

nameAndSurname(name, surname)