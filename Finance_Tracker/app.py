from utils import display_menu
### Step 1: Menu System (30 minutes)
# Create the basic menu loop:
# - Display menu options
# - Get user input
# - Use if/elif to handle choices
# - Add exit option


def main()-> None:
    display_menu()
    while True:
        user_input = input("> ")
        if user_input == "8":
            print("Exiting program...")
            break
        elif user_input == "9":
            display_menu()
        else:
            print("Invalid choice, please enter a number from 1 to 9")

main()