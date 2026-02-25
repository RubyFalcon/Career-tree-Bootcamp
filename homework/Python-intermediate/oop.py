from car import Car
# Object = A "bundle" of related  attributes(variables) and methods (functions)
# e.g. phone, cup, book

# class = (blueprint) used to design the structure and layout of an object


car1 = Car("Bmw", 1995,"Blue", False)
car2 = Car("Mustang", 1995,"Blue", False)
car3 = Car("Bmw", 1995,"Blue", False)


print(car1.color)

car1.drive()
car1.stop()

car1.describe()