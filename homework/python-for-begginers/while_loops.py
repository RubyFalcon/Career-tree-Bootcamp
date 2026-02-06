# while loops to execute block of codes multiple times
i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")

# Ex: use a while loop to make a guessing game
 
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit: 
    guessed_num = int(input("guess a number: "))
    guess_count += 1
    if guessed_num == secret_number:
        print("You won!")
        break
else: #else in while will run if we execute to completion
    # without any break
    print("Sorry, you failed!")

