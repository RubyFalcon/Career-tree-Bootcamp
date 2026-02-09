# Constructors: 
class Point:
    def __init__(self, x , y): #x __init__ used to construct an object
        #self refers to instance of object
        self.x = x
        self.y = y    
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")
    
point1 = Point(10,20)
print(point1.x)
point1.y = 15
print(point1.y)

# 01: Define person with -name atrr, -talk() method
class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hello my name is {self.name}")
    
john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()