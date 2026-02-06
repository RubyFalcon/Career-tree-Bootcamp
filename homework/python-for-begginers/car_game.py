print("Welcome to car game, type 'help' for all commands")

command = ""
car_running = False
while True:
    command = input("> ").lower()
    if command == "quit":
        break
    elif command == "help":
        print("\nstart - to start the car\nstop - to stop the car\nquit - to exit")
    elif command == "start":
        if not car_running:
            print("Car started... ready to go!") 
            car_running = True
        else:
            print("Car already started!")
    elif command == "stop":
        if car_running:
            print("Car stopped.")
            car_running = False
        else:
            print("Car already stopped!")

    else:
        print("I don't understand that")
