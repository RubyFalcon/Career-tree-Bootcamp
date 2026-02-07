# Lists are mutable
empty_list = []

fruits = ["apple", "banana", "strawberries", "mango", "kiwi", "blueberry" ]

mixed = [True,1,2,3.4,"John"]

letters = list("Python") #using list constructor to create a list, new keyword not used in python
# print(letters)

numbers = list(range(1,8))
print(numbers) # [1, 2, 3, 4, 5, 6, 7]

reversed_numbers = list(range(8,4,-1)) #[8,7,6,5]

# Just like with strings we can use [:] to access a range of items from a list
# print(reversed_numbers [:3]) # [1, 2, 3]


# print(dir(list)) # ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# dir shows the methods in the list class, we have removed the dunder methods for now

numbers.append(100)
print(numbers) # 1, 2, 3, 4, 5, 6, 7, 100]
numbers.extend([10,20,30]) # adding multiple 
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 100, 10, 20, 30]
numbers.remove(20) 
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 100, 10, 30]


print(fruits) # ['apple', 'banana', 'strawberries', 'mango', 'kiwi', 'blueberry']
position = fruits.index("mango")
print(position) # 3

# position1 = fruits.index("mango"  ,  4) -> error, index out of range
print(fruits.count("mango")) # 1 

print(len(fruits)) # 6

# adding 2 lists together
fruits = ['apple', 'banana']
more_fruits = ['orange', 'kiwi']
combined_fruits = [*fruits, *more_fruits]

print(combined_fruits)  # Output: ['apple', 'banana', 'orange', 'kiwi']