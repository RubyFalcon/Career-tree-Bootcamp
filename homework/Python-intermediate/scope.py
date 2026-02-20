# Variable scope - where a variable is visible and  accessible 
# Scope resolution = (LEGB) = Local -> Enclosed -> Global -> Built-in

def func1():
    x = 1
    
    def func2():
        
        print(x)
    func2()

func1() #will print 1 since x is not defined local, it goes to enclosed