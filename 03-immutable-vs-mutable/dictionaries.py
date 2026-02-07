# Dictionaries
# Dictionaries are mutable
# Can you turn dict into JSON?
empty_dict = {}
student = {
    "name": "John",
    "grade": "A",
    "Subjects": ["Maths", "Science", "CompSci"],
    "phone" : 6912345
}

print("Student Dictionary", student)

person =  {
    "name": "Robert",
    "height": 180.2,
    "is_student": False,
    "address": {
        "street": "13 main steet",
        "city": "London",
    }
}

print(person["address"]["street"])
# print(person["name11"]) #results in an error
print("Name", person.get("name", "No Such key")) 

# Modify a Dictionary 
my_dict = {
    "first_name": "Narayan",
    "last_name": "Khosla"
}

# add single item to dict
my_dict["age"] = 50 #add a new key:value to my_dict
print(my_dict)

# add multiple items
my_dict.update({"email": "email@email.com", "phone": 765231}) #add multiple key_values to my_dict
print(my_dict)

# remove item from dict
del my_dict["age"]
print(my_dict)

my_dict["age"] = 55
print(my_dict)

print(my_dict.pop("age"))
my_dict.pop("age2", "no column found") # no column is a placeholder for if we dont find it, returned but not printed
print(my_dict.get("age2", "not found"))
print(my_dict)

print(my_dict.pop("age2", "no column found"))
# print(dir(dict)) # ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# Combine two dicts