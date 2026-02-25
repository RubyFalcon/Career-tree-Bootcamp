# class variables = Shared among all instances of a class
#                   Defined outside the constructer
#                   Allow you to share data among all objects created from the class

class Student:
    class_year = 2024 #class year is a class variable
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrik", 35)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(student1.class_year)
print(Student.class_year) # good practice to access class variables by their class
print(Student.num_students)