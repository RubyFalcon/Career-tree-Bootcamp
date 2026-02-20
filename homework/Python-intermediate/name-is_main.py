# if __name__ = __main__ (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice: (Code modular
#  helps readability, 
# leaves no global variables,
# avoid unintended execution
# )

def favorite_food(food):
    print(f"Your favourit foos is {food}")

def main():
    print("Hahaha we printed this")
    favorite_food("Pizza")
    print('end of name_is_main.py')

if __name__ == "__main__": #name= main means we are running this specific python file
    main()
