
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
    UPDATABLE_FIELDS = {
        "first_name",
        "last_name",
        "age",
        "subjects",
        "details",
    } 

    def update(self, **updates):
         
        """
        Safely updates allowed fields only:
          - first_name (str)
          - last_name (str)
          - age (int, 1..120-ish)
          - subjects (iterable of str)
          - details (dict) -> merges into existing details

        Defensive programming:
          - rejects unknown fields
          - validates types + basic constraints
          - does not partially update if errors found
        """
        if not isinstance(updates, dict):
             raise TypeError("updates must be keyword arguments (a dict-like set of kwargs).")
        
        unknown = set(updates) - self.UPDATABLE_FIELDS
        if unknown:
            raise ValueError(f"Cannot update fields: {sorted(unknown)}. "
                             f"Allowed: {sorted(self.UPDATABLE_FIELDS)}")
        
        errors = []

        # Stage changes first (so we don't partially update on error)
        staged = {}

        # first_name
        if "first_name" in updates:
            fn = updates["first_name"]
            if not isinstance(fn, str) or not fn.strip():
                errors.append("first_name must be a non-empty string.")
            else:
                staged["first_name"] = fn.strip()

        # last_name
        if "last_name" in updates:
            ln = updates["last_name"]
            if not isinstance(ln, str) or not ln.strip():
                errors.append("last_name must be a non-empty string.")
            else:
                staged["last_name"] = ln.strip()

        # age
        if "age" in updates:
            age = updates["age"]
            if not isinstance(age, int):
                errors.append("age must be an int.")
            elif age < 1 or age > 120:
                errors.append("age must be between 1 and 120.")
            else:
                staged["age"] = age

        # subjects (replace subjects list)
        if "subjects" in updates:
            subs = updates["subjects"]
            if subs is None:
                # allow clearing subjects
                staged["subjects"] = []
            elif isinstance(subs, (list, tuple, set)):
                cleaned = []
                for s in subs:
                    if not isinstance(s, str) or not s.strip():
                        errors.append("subjects must contain only non-empty strings.")
                        break
                    cleaned.append(s.strip())
                else:
                    staged["subjects"] = cleaned
            else:
                errors.append("subjects must be a list/tuple/set of strings (or None to clear).")

        # details (merge dict)
        if "details" in updates:
            det = updates["details"]
            if det is None:
                staged["details"] = {}  # allow clearing details
            elif not isinstance(det, dict):
                errors.append("details must be a dict (or None to clear).")
            else:
                # merge, don't replace
                staged["details_merge"] = det
        
        if errors:
            # Defensive: no partial updates
            raise ValueError("Update rejected:\n- " + "\n- ".join(errors))

        # Apply staged updates
        for k, v in staged.items():
            if k == "details_merge":
                self.details.update(v)
            else:
                setattr(self, k, v)

        return True