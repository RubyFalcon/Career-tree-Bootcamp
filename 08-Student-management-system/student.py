
class Student: 
    def __init__(self, id: int , first_name: str, last_name:str, age:int, address:str, school_year:int,scores:dict = {},*subjects, **details):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address 
        self.school_year = school_year
        self.subjects = list(subjects)
        self.details = details
        self.scores = scores

    def __str__(self):
        return f"id:{self.id}\n name: {self.first_name} {self.last_name} \n, Age {self.age} \nYear {self.school_year} \nScored: {self.scores} \nSubjects: {self.subjects} \ndetails: {self.details} "

    def __repr__(self):
        return self.__str__()
    def add_score(self, subject,score):
        self.scores[subject] = score