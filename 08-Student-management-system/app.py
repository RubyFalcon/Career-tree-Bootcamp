# Create a student management system
# 01: 
# Create a wat to store multiple students in your program
from student import Student

class School:
    def __init__(self, students: dict[Student] | None = None):
        self.students = students if students is not None else {}

    def add_student(self,student:Student):
        if student.id in self.students:
            print("Student already exists")
            return
        self.students[student.id] = student
    def remove_student(self, student_id):
        removed = self.students.pop(student_id, None)
        if removed is None:                          
            print("Student not found")
        else:
            print(f"{removed.first_name} was removed")
        return removed
    def get_students(self):
        return list(self.students.values())
    
    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        headers = ["ID", "First", "Last", "Age", "Year", "Avg Score","Address"]

        rows = []
        for s in self.students:
            avg = sum(s.scores.values()) / len(s.scores) if s.scores else 0
            rows.append([
                s.id,
                s.first_name,
                s.last_name,
                s.age,
                s.school_year,
                f"{avg:.2f}",  # formatted average
                s.address,
            ])

        # column widths = max of header/values per column
        col_widths = []
        for col_idx in range(len(headers)):
            col_widths.append(
            max(len(str(headers[col_idx])), max(len(str(r[col_idx])) for r in rows))
            )

        def fmt_row(row):
            return " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row))


        line = "-+-".join("-" * w for w in col_widths)
        print(fmt_row(headers))
        print(line)
        for r in rows:
            print(fmt_row(r))
            
    def find_student_by_id(self, student_id):
        return self.students.get(student_id)
        
    def add_student_score(self,student_id,subject,score):
        student = self.find_student_by_id(student_id)
        if student is not None:
            student.add_score(subject, score)
        else:
            print("Student not found")
            return
        
    def find_student_by_name(self, name:str):
        name = name.strip().lower()
        return [s for s in self.students.values() if s.first_name.lower() == name]
    
    def get_average_scores(self, student_id):
        student = self.find_student_by_id(student_id)
        if student is None:
            print("Student not found")
            return None
        return student.get_average_score()
    
    def get_top_student(self):
        students_with_scores = [s for s in self.students if s.scores]
        if not students_with_scores:
            return None
        return max(students_with_scores, key=lambda s:sum(s.scores.values())/ len(s.scores))
    




def main():
    my_school = School()
    my_school.add_student(Student(1,"John","Doe", 16, "123 Adress", 11,"maths", "english"))
    my_school.add_student(Student(1,"John","Smith", 13, "123 Adress", 8,"maths", "english"))
    my_school.add_student(Student(2,"Joe","Weller",15,"145 Address", 10,"Economics", "English",))
    my_school.add_student(Student(3,"Super", "Man",17,"566 noting hill", 13,"Maths"))

    # print(my_school.get_students())
    my_school.find_student_by_id(1)
    my_school.add_student_score(1,"Maths", 90)
    my_school.add_student_score(1,"English", 60)
   
    print(my_school.find_student_by_id(1))
   
    matches = my_school.find_student_by_name("John")
    for s in matches:
        print(s)
    # print(my_school.get_average_scores(1))
    # my_school.display_students()
    # print(my_school.get_top_student())
if __name__ == "__main__": #name= main means we are running this specific python file
    main()



#find the top scorer from school