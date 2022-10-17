def legalAge(user):
    return user.age > 17

class User:
    def __init__(self,age):
        self.age = age

age = int(input('Type your age: '))
while age < 0 or age > 120:
    print('ERROR...Type a valid age')
    age = int(input('Type your age: '))

user = User(age)

isLegal = legalAge(user)

print(isLegal)