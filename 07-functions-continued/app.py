# interview: what is the shortcomings of this function:



# 1. we can cause errors for string assignments

# def add(n1:int,n2:int):
#     if type(n1) or type(n2) is str:
#         print("type cannot be string")
#     else:
#         return n1 + n2

# print(add('sting', "bob"))

# 2. we might want more than 2 numbers

def add(*nums):
    return sum(nums)

print(add(2,2,2,))

# Lambda functions
def square(x):
    return x*x

# using lambda
my_square = lambda y: y* y

my_add = lambda *nums : sum(nums)

print(my_add(1,2,3))