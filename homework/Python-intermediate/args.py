# *args - allows to pass non-key arguments
# **kwargs - allows to pass multiple key-word arguments
#       * - unpacking operator
#       1.Positional 2. default 3. keyword 4. Arbitrary

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

def print_address(**kwargs):
    pass

print_address(street="123 Notting Hill", city="Notting Hill", area="",post_code="Ww12 33d")