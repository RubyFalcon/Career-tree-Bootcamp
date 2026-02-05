# Mutability vs immutabiltiy 

# Strings are immutable

name = "Ryan"
name1 = "Narayan"

statement = "I need to return's Alice's Book"
statement2 = 'Alice\'s Dog '  #we can use escape characters \ to add in ' or "" , we can also use \t to create a tab \n or to add a \ we use \\
statement3 = ''' Alice's Dog said : "Woof Woof" 
As we mentioned
'''  # called a multi string - lets us write a string on multi lines , and it recognize new lines

print(statement3)

# len method
password = input("Enter your password: ")
pass_length = len(password)
if pass_length <= 8:
    print("Sorry, not strong enough")

last_char = password[-1] #gives last character

post_code  = "CV2 7ED"
area_code = post_code[:3] #gives us the chars from index 0 -> 3 but not including 3 , can also type as post_code[0:3]

text1 = "Python programming is one of the best languages" 
print(text1[1:30:3])
          #[start: end: step] 

str5 = "Narayan Khosla"
# print every even character
print(str5[1: len(str5):2])  #option 1
print(str5[1:: 2])  #option 2 pythonic way

# Q: reverse a string
str6 = "palindrome" 
print(str6[::-1]) # emordnilap

# careful with -0, 