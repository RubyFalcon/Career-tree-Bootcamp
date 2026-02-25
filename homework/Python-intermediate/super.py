# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods
class Shape:
    def __init__(self, color:str, is_filled: bool):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not_filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
    def describe(self):
        print(f"It is a circle with an area of {self.area()}")
        super().describe()


class Square(Shape):
    def __init__(self, color:str, is_filled:bool, width: int ):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width**2}")
        super().describe()



class Triangle:
    def __init__(self, color:str, is_filled:bool, width:int, height:int):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle = Circle("Red", True,5)
print(circle.color)
print(circle.is_filled)
print(circle.radius)
print(circle.area())
circle.describe()