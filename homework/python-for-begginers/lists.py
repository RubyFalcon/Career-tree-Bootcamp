names = ["John", "Bob", "Mosh", "Sarah", "May"]
print(names[-1]) #last item
# Can use colon : to select a range of items, creates a new list without affecting the og list
print(names[2:]) #['Mosh', 'Sarah', 'May']

# Modify list
names[0] = 'Jon'

# O1 : Find the largest number in a list

numbers = [1,2,6,7,10,3]

largest_number = numbers[0]
for num in numbers:
    if num > largest_number:
        largest_number = num
print(largest_number)
    
# 2d lists: A list where each item is another list

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# find 1st element:
print(matrix[0][0])
# find last element:
print(matrix[-1][-1])

# iterate over matrix:
for row in matrix:
    for item in row:
        print(item)
