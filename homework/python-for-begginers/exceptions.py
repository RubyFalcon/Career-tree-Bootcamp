# How to handle errors:
# 01: use try except (known as try catch in other languages) so exception errors dont crash our code


try:
    age = int(input("Age:  "))
    income = 20000
    risk = income/ age #will crash if we have age 0
    print(age) 
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Ivalid value")

