class Animal:
    def __init__(self, name, noise):
        self.name = name
        self.noise = noise
    def greetings(self):
        print(self.animalType + " name: " + self.name + " and make this sound: " + self.noise)

class Cat(Animal):
    animalType = 'cat'
    def __init__(self, name, noise):
        Animal.__init__(self, name, noise)
        print("Extending the __init__ method in Cat class")

class Dog(Animal):
    animalType = 'dog'
    def __init__(self, name, noise):
        super().__init__(name, noise)
        print("Creating an instance for <<Dog>> and extending the <<__init__>> method")
        #we extend the __init__ method to make changes with the same variables

class Fish(Animal):
    animalType = 'fish'

cat = Cat("Misifus", "Miau")
cat.greetings()
dog = Dog("Spike", "Guaf")
dog.greetings()
fish = Fish("Gumppy", "Glump glump")
fish.greetings()