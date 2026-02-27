import transactions

def display_menu():
    print("\n" + "=" * 40)
    print("         💰 Finance Tracker")
    print("=" * 40)
    print("1) Add Income")
    print("2) Add Expense")
    print("3) View All Transactions")
    print("4) View Summary")
    print("5) View by Category")
    print("6) Set Monthly Budget")
    print("7) Clear All Data")
    print("8) Exit")
    print("9) Help")
    print("=" * 40)
    
def input_command():   
    '''gets an input from 1-9 in order to run some commands'''
    while True:
        print("\n"+ "=" * 50)
        user_input = input("Choose an option (1-9): ").strip()
        match user_input:
                case "1":
                    transactions.add_income()
                
                case "2":
                    transactions.add_expense()
        
                case "3":
                    transactions.view_all_transactions()
                    
                case "4":
                    transactions.calculate_summary()
                    
                case "5":
                    transactions.view_by_category()
                    
                case "6":
                    transactions.set_budget()
                    
                case "7":
                    transactions.clear_all_data()
                    
                case "8":
                    print("Exiting program...")
                    break
            
                case "9":
                    display_menu()

                case _:
                    print("Invalid choice, please enter a number from 1 to 9")

        display_menu()