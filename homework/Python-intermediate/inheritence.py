# Inheritence  = allows a class to inherit attribute and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def speak():
        print("Squeak")


class Mouse(Animal):
   def speak():
        print("Meow")


dog = Dog("Scooby")
cat = Cat("Garfield")
print(dog.name)
print(dog.is_alive)
print(cat.name)
print(cat.is_alive)
cat.eat()