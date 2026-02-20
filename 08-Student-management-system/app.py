# Create a student management system
# 01: 
# Create a wat to store multiple students in your program
from student import Student

class School:
    def __init__(self, students: list | None = None):
        self.students = students if students is not None else []

    def add_student(self,student:Student):
        self.students.append(student)
    
    def get_students(self):
        return self.students


def main():
    print("got here")
    my_school = School()

    my_school.add_student(Student(1,"John","Doe", 16, "123 Adress", 11))
    my_school.add_student(Student(2,"Joe","Weller",15,"145 Address", 10))
    my_school.add_student(Student(3,"Super", "Man",17,"566 noting hill", 13))

    print(my_school.get_students())

if __name__ == "__main__": #name= main means we are running this specific python file
    main()
