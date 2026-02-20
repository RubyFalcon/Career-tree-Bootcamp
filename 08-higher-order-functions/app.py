# Higher Order Functions
# A HOF takes another Function as an argument/ reutnrs function as its result

def uppercase(text:str):
    return text.upper()

def whisper(text:str):
    return text.lower()

def greet(func):
    message = func("Hello World")
    print(message)

greet(uppercase)
greet(whisper)

print(type(greet))

numbers = [1,2,3,4,5,6,7]

# map, filter, reduce, sort
def square(n):
    return n * n

def is_odd(n):
    return n % 2 != 0

res1 = list(filter(is_odd, numbers))
print(res1)
# using lambda function:
res2 = list(filter(lambda x:  x %2 != 0, range(1,8)))
print(res2)

squared = list(map(lambda n : n*n , range(1,10)))

print(squared)