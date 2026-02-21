# Create a student management system
# 01: 
# Create a wat to store multiple students in your program
from student import Student

class School:
    def __init__(self, students: list[Student] | None = None):
        self.students = students if students is not None else []

    def add_student(self,student:Student):
        self.students.append(student)
    
    def get_students(self):
        return self.students
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student_id == student.id:
                return student
        else:
            return None
        
    def add_student_score(self,student_id,subject,score):
        student = self.find_student_by_id(student_id)
        if student is not None:
            student.add_score(subject, score)
        else:
            print("Student not found")
            return
    def find_student_by_name(self, name):
        return [ student for student in self.students
                if student.first_name.lower() == name.lower()]
    def get_average_scores(self, student_id):
        student = self.find_student_by_id(student_id)
        if student is None:
            print("Student not found")
            return None

        if not student.scores:  
            return 0

        total = sum(student.scores.values())
        count = len(student.scores)
        return f"{student.first_name}'s average score is : {total / count}"


def main():
    print("got here")
    my_school = School()

    my_school.add_student(Student(1,"John","Doe", 16, "123 Adress", 11,"maths", "english"))
    my_school.add_student(Student(1,"John","Smith", 13, "123 Adress", 8,"maths", "english"))
    my_school.add_student(Student(2,"Joe","Weller",15,"145 Address", 10,"Economics", "English",))
    my_school.add_student(Student(3,"Super", "Man",17,"566 noting hill", 13,"Maths"))

    # print(my_school.get_students())
    my_school.find_student_by_id(1)
    my_school.add_student_score(1,"Maths", 90)
    my_school.add_student_score(1,"English", 60)
    # print(my_school.find_student_by_id(1).scores)
    print(my_school.find_student_by_name("John"))
    print(my_school.get_average_scores(1))
if __name__ == "__main__": #name= main means we are running this specific python file
    main()



# find a student by name - match all names