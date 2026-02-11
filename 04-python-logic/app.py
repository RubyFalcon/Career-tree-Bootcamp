# Dicts
student = {"name":"Alice", "age": 20, "grade": "A"}

if "name133" in student:
    print("yay")

if "Alice" in student.values():
    print("We found Alice")

users = {
    "alice": "Password234",
    "bob": "secret 66",
    "charlie": "pass5455"
}

# username = input("\n Enter a username: ")
# password  = input("\n Enter a password: ")

# if username in users:
#     if users[username] == password:
#         print("Login Successfull")
#     else: 
#         print("Incorrect Password")  
# else:
#     print("Username doesn't exist")
    

student_users = {**student, **users}

dict1 = {"name": "Narayan", "language": "Python", "city": "London"}
dict2 = {"empId" : "101", "canDrive" : True, "hobby": "Cricket"}

# using update:

dict3 =  dict1.copy()
dict3.update(dict2)


# using unpacking(similar javascript spread operator) : ** for dicts, * for lists
dict3 = {**dict1, **dict2}

# using pipe symbol
dict3 = dict1 | dict2

# print(dir(dict)) # to acces all the methods

# Tuples - immutable, usully with (val,val)
coordinates = (89,12)
empty_tuple = () 
one_value = (78,) #to make one value we must add the ,


my_fruits = ("apple", "pineapple", "guava", "kiwi", "blueberries")

# 01: how to get length?
fruits_length = len(my_fruits)

# indexing works
print(my_fruits[0])
print(my_fruits[-1])


# use slicing
print(my_fruits[0::2])
print(my_fruits[-2::-1])

# mon,tue,wen,thur,fri = my_fruits
mon,tue,wen = my_fruits[0:3]
print(mon)
print(tue)
print(wen)

numbers = (1,2,3,4,5,6,7,8,9)
first,*middle,last = numbers

first,middle, last = numbers[0:9:3]

print(first)
print(middle)
print(last)

# show tuples are immutable :
# Erorr handle method so we don't break our code
print(id(f"Memory address: {numbers}"))
try:
    numbers[0] = 15
except TypeError:
    print("Tuples are immutable")
numbers = (1,2,5,6)
# can also throw new errors in python

# hw: tuples with mutable objects, 

data = (1,2,3,[4,5])
# the mutable data in a tuple is stil mutable
data[3][0] = 2
data[3].append(67)
print(data)



