
# If it's a hot day
    # It's a hot day
    # Drink plenty of water
# otherwise if it's cold
    # It's a  cold day
    # Wear warm clothes
# otherwise
    # It's a lovely day

# 01: Define a boolean variable
is_hot = False
is_cold = False
# 02: Add condition
if is_hot:
    print("It's a hot day \nDrink plenty of Water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


# Exercise 01: print the down payment needed for buyer
# with good credit
house_price = 1000000
good_credit = True

if good_credit:
    down_payment = round(house_price * 0.1) #10%    
else:
    down_payment = round(house_price * 0.2) #20% 
print(f"Down payment: ${down_payment}")

# Comparison operators

name = "J"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 15:
    print("Name must be a maximum of 15 characters")
else:
    print("Name looks good")