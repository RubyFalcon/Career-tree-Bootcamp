# Classes: used to define reusable complex objects to model real concepts
class Point: # Pascal case for naming classes e.g; EmailClient
    # methods:functions called on object point1.move()
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")
    
    




# Object is an instance of class
point1 = Point()

# attributes: variables belonging to an object
point1.x = 10
point1.y = 20

point1.draw()

point2 = Point()
print(point1.x)
# print(point2.x) #error , x not defined, 

