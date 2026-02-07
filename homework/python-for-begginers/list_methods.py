numbers = [5,2,1,7,4]

# append: add to end of lis
numbers.append(20)
print(numbers)

# insert(): add number at index
numbers.insert(0,10)
print(numbers)

# remove
numbers.remove(5)
print(numbers)

# index: index of number
# print(numbers.index(7))

# print(50 in numbers) # False

# Sort: sorts numbers
numbers.sort()
# Reverse: sorts in desc order
numbers.reverse()
# print(numbers)

numbers2 = numbers
numbers3 = numbers.copy()
numbers.append(10) #this will also append 10 to numbers2

# print(numbers2) # [20, 10, 7, 4, 2, 1, 10]
# print(numbers3) # [20, 10, 7, 4, 2, 1]

# 01: Remove duplicates from a list
duplicates = [2,5,3,2,2,6,8,9,9,10,2]
uniques = []
print(numbers)
for number in duplicates:
    if number not in uniques:
        uniques.append(number)

print(uniques)