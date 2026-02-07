# Dictionaries: used to create key,value pairs , mutable
# Keys must be unique
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified" : True,
    "email": "john@gmail.com",
    "number" : "542133",    
}

print(customer["name"])
print(customer.get("birthdate"))
print(customer.pop("birthdate", "None"))

customer["name"] = "Jack Smith"
customer["birthdate"] = "Dec 26 1999"

# 01: Create a dictionary which takes numbers and converts into named numbers

number_dict = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
phone_number = input("Phone: ")
output = ""
for number in phone_number:
    if number in number_dict.keys():
        output += number_dict[number] + " "

print(output)