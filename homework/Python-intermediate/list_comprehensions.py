# List comprehension = Concise way to create lists in Python
                    # Compact and easier to read than loops
#                   [expression for value in iterable if condition]

# Traditional for loop method
doubles = []
for x in range(1,11):
    doubles.append(x*2)

new_doubles = [x*2 for x in range(1,10)]
print(new_doubles)

fruits = ["apple","orange", "banana", "coconut"]

fruit_chars= [fruit[0]for fruit in fruits]

print(fruit_chars)

numbers = [0,2,-3,-1, 6,-10,7]

positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num %2 == 0]

print(positive_nums)
print(negative_nums)
print(even_nums)

print(help("math"))