# Get weight
weight = input("Weight: ")
# Get unit lbs or kg
unit = input("(L)bs or (K)g: ")

if  unit.upper() == "L":
    weight_in_kg = int(weight) * 0.453
    print(f". You are {weight_in_kg} kilos")
elif unit.upper() == "K":
    weight_in_lbs = int(weight) * 2.205
    print(f"You  are {weight_in_lbs} pounds")