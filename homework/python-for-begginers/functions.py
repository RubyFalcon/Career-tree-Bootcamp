#  As we make more code, we need to make functions 
# Function: Container for code block to do a specific task, print, input are functions
# Cannot be called before being defined in python
def greet_user(): #def defines a function
    print("Hi there!")
    print("Welcome aboard!")


print("Start")
greet_user()
print("Finished")

# Parameters : we can add parameter to functions to pass information to our functions

def greet_user(name = "John", surname = "Doe"): #def defines a function with an argument. we give it a default value
    print(f"Hi there {name} {surname}!")
    print("Welcome aboard!")

greet_user("Adam", "Smith")
greet_user()
greet_user(surname="Apple",name="Berry") #using keyword arguments help to apply context

# E.g. numerical arguments to increase readability
# calc_cost(total=50, shipping=5, discount=0.1) #readable and understsandable to non technical users

# Key word arguments must come after positional argument, if both are used

# Returns: we use return to return a result to whoever uses a function
# Default return is None

def square(num):
    return num * num

print(square(3))

# Reusable function

# 01: turn emoji into a function

message = input("> ")

def convert_emojis(text):
    words = text.split(" ")
    emojis = {
    ":)": "😊",
    ":(": "☹️",
    ":P": "😋",
    ":D": "😀",
}

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

print(convert_emojis(message))