finances = {
    "income": 0,
    "expenses": 0,
    "transactions": [],

}
# TODO: separate logic of add_income into get_income_input and add_income
def add_income():
    """Add a new income transaction"""
    category = input('Category - Salary, Freelance, Gift: \n> ').lower()
  
    if category == "salary" or category == "freelance" or category == "gift":
        amount = input("Enter amount: £ \n> ")        
        if float(amount) > 0:
            converted_amount = float(amount)
            finances["income"] += converted_amount
            finances["transactions"].append({"transaction_type":"income","category": category, "amount": converted_amount})
        else:
            print("Amount was incorrect")
    else:
        print("wrong input")

def add_expense():
    amount = float(input("Enter an amount: £"))
    converted_amount = float(amount)
    finances["expenses"] += converted_amount
    finances["transactions"].append({"transaction_type":"expense", "amount": converted_amount})

def view_all_transactions():
    for transaction in finances["transactions"]:
        print(transaction)

def calculate_summary():
    print(f"Our total is £{finances['income'] - finances['expenses']}")

def view_by_cagegory():
    pass
def set_budget():
    pass