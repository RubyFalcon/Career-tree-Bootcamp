def display_menu():
    print('''
1. Add Income
2. Add Expense
3. View All Transactions
4. View Summary
5. View by Category
6. Set Monthly Budget
7. Clear All Data
8. Exit
9. Help

''')
    
def input_command():
    '''gets an input from 1-9 in order to run some commands'''
    while True:
        print("=" * 50)
        user_input = input("> ")
        match user_input:
                case "1":
                    # add_income()
                    pass
                case "2":
                    # add_expenses()
                    pass
                case "3":
                    # view_all_transactions()
                    pass
                case "4":
                    # calculcate_summary()
                    pass
                case "5":
                    # view_by_category()
                    pass
                case "6":
                    # set_budget()
                    pass
                case "7":
                    # clear_all_data()
                    pass
                case "8":
                    print("Exiting program...")
                    break
                case "9":
                    display_menu()
                case _:
                    print("Invalid choice, please enter a number from 1 to 9")