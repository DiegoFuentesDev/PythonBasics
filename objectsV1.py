class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def greetings(self):
        print('My name is: ' + self.name + ' and my surname is: ' + self.surname)

class Admin(User):
    def superGreetings(self):
        print("I'm " + self.name + " the admin")


user = User('New Name', 'New Surname')
user2 = User('New Name2', 'New Surname2')

admin = Admin('Spider', 'Man')
# del user2.name
# del user2.surname

user.greetings()
user2.greetings()

admin.greetings()
admin.superGreetings()