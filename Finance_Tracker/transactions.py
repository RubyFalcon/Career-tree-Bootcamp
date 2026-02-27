from datetime import datetime
import os
DATA_FILE = "transactions.txt"
finances = {
    "income": 0,
    "expenses": 0,
    "transactions": [],

}


# TODO: separate logic of add_income into get_income_input and add_income

def load_transactions(filename=DATA_FILE):

    # 1) reset memory state (so calling twice doesn't double totals)
    finances["income"] = 0
    finances["expenses"] = 0
    finances["transactions"] = []

    # 2) if file doesn't exist yet, we’re done (defaults remain 0 / empty)
    if not os.path.exists(filename):
        return
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # timestamp,type,category,amount
            timestamp, t_type, category, amount = line.split(",")
            amount = float(amount)

            # rebuild transactions list
            finances["transactions"].append({
                "transaction_type": t_type,
                "category": category,
                "amount": amount,
                "timestamp": timestamp,
            })

            # rebuild totals
            if t_type == "income":
                finances["income"] += amount
            elif t_type == "expense":
                finances["expenses"] += amount

# save transactions
def save_transaction(transaction_type, category, converted_amount: float, filename=DATA_FILE):
    """
    Appends a single transaction to a text file as CSV:
    timestamp,type,category,amount
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Always write with newline at end; format amount to 2dp for £
    line = f"{timestamp},{transaction_type},{category},{converted_amount:.2f}\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(line)

    print(f"{transaction_type} of £{converted_amount: .2f} recorded successfully")

def add_income():
    """Add a new income transaction"""
    categories = ["salary", "freelance", "gift"]
    category = input('Category - Salary, Freelance, Gift: \n> ').lower().strip()
    try:
        if category in categories:
            amount = input("Enter amount: £ \n> ")        
            if float(amount) > 0:
                converted_amount = float(amount)
                finances["income"] += converted_amount
                finances["transactions"].append({"transaction_type":"income","category": category, "amount": converted_amount})
                save_transaction("income", category, converted_amount)
            else:
                print("Amount was incorrect")
        else:
            print("wrong input")
    except ValueError:
        print("Invalid amount. Returning to menu")

    # TODO: Save transaction with the correct category and amount

def add_expense():
    categories = ["food", "transport", "bills"]
    category = input('Category - food, transport, bills: \n> ').lower().strip()
    try:
        if category in categories:
            amount = input("Enter an amount: £")
            if float(amount) > 0:
                converted_amount = float(amount)
                finances["expenses"] += converted_amount
                finances["transactions"].append({"transaction_type":"expense","category": category, "amount": converted_amount})
                save_transaction("expense", category, amount)
    except ValueError:
        print("Invalid amount. Returning to menu")
    
def view_all_transactions():
    for transaction in finances["transactions"]:
        print(transaction)

def calculate_summary():
    print(f"Our total is £{finances['income'] - finances['expenses']}")

def view_by_cagegory():
    pass
def set_budget():
    pass

