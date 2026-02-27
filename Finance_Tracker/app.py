from utils import display_menu, input_command
from transactions import load_transactions
### Step 1: Menu System (30 minutes)
# Create the basic menu loop:
# - Display menu options
# - Get user input
# - Use if/elif to handle choices
# - Add exit option


def main()-> None:
    load_transactions()
    display_menu()
    input_command()

        
            
if __name__ == "__main__":
    main()