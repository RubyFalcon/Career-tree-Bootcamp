
class Student: 
    def __init__(self, id: int , first_name: str, last_name:str, age:int, address:str, school_year:int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address 
        self.school_year = school_year

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}, Age {self.age}, Year {self.school_year}"
    
    def __repr__(self):
        return self.__str__()