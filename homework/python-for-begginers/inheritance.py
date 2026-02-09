# Inheritence in python: mechanism to reuse code 
# Both Dog cat want to walk()
class Mamal:
    def walk(self):
        print("Walk")

class Dog(Mamal): #Dog extends Mamal, inherit all methods from Mamal
    def bark(self):
        print("Bark")
    pass


class Cat(Mamal):
    def meow(self):
        print("Meow")
    pass

dog1 = Dog()
dog1.walk()

cat1 = Cat()