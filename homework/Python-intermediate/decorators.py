# Decoratoe = A function that extends the behaviour of another function
#             w/o modifying the base function
#             pass the base function as an argument to the decorator

#             @add_sprinkes
#             get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("* You add sprinkles 🎊")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("You add fudge! 🍫")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor:str):
    print(f"Here is your {flavor} Ice cream 🍦")

get_ice_cream("Chocolate")