
class Student: 
    def __init__(
            self, 
            id: int,
            first_name: str,
            last_name:str,
            age:int, address:str,
            school_year:int,
            scores:dict = {},
            *subjects,
            **details,
            ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address 
        self.school_year = school_year
        self.subjects = list(subjects)
        self.details = details
        self.scores = {}
     
    def get_average_score(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)
    
    def _row(self):
        avg = self.get_average_score()
        name = f"{self.first_name} {self.last_name}"
        return (
            f"{self.id:<4} | "
            f"{name:<20} | "
            f"{self.age:<3} | "
            f"{self.school_year:<4} | "
            f"{avg:>7.2f}"
    )

    def __str__(self):
        return self._row()
    
    def __repr__(self):
        return self._row()
    
    def add_score(self, subject,score):
        self.scores[subject] = score