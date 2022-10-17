def legalAge(age):
    if age < 18:
        return print('Child')
    else:
        return print('Adult')

age = int(input('Type your age: '))
while age < 0 or age > 120:
    print('Type a valid age')
    age = int(input('Type your age: '))

legalAge(15)