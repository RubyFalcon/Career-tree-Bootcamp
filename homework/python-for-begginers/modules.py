# Modules: python files to be important/exported to different 
import converters
# or
from converters import kg_to_lbs, lbs_to_kg

print(kg_to_lbs(70))
print(lbs_to_kg(180))
print(converters.kg_to_lbs(70))


# 01: create utils.py and def and import find_max, takes a list, returns greatest num
from utils import find_max
numbers = [10,3,4,5,1,0]

max_num = find_max(numbers)
print(max_num)
# or we can use built in max
print(max(numbers))