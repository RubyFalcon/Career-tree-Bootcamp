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
                save_transaction("expense", category, converted_amount)
    except ValueError:
        print("Invalid amount. Returning to menu")
    
def view_all_transactions():
    txs = finances["transactions"]

    if not txs:
        print("No transactions yet.")
        return

    # Column headers
    headers = ["#", "Date/Time", "Type", "Category", "Amount (£)"]

    # Build rows
    rows = []
    for i, t in enumerate(txs, start=1):
        timestamp = t.get("timestamp", "N/A")
        t_type = t.get("transaction_type", "N/A")
        category = t.get("category", "N/A")
        amount = float(t.get("amount", 0.0))
        rows.append([str(i), timestamp, t_type, category, f"{amount:.2f}"])

    # Compute column widths (max of header vs all rows)
    col_widths = []
    for col_idx in range(len(headers)):
        max_len = len(headers[col_idx])
        for r in rows:
            max_len = max(max_len, len(r[col_idx]))
        col_widths.append(max_len)

    def format_row(values:str):
        return " | ".join(v.ljust(col_widths[i]) for i, v in enumerate(values))

    separator = "-+-".join("-" * w for w in col_widths)

    # Print table
    print(format_row(headers))
    print(separator)
    for r in rows:
        print(format_row(r))

def calculate_summary():
    print(f"Our total is £{finances['income'] - finances['expenses']}")

def view_by_category():
    # Optional: ensure you’re looking at the latest data from file
    # load_transactions()
    category = input("Enter category: \n> ").lower().strip()

    matches = [t for t in finances["transactions"] if t.get("category") == category]

    if not matches:
        print(f"No transactions found for category: {category}")
        return

    income_total = 0.0
    expense_total = 0.0

    print(f"\nTransactions for category: {category}\n" + "-" * 50)
    for t in matches:
        t_type = t.get("transaction_type")
        amount = float(t.get("amount", 0))
        timestamp = t.get("timestamp", "N/A")

        if t_type == "income":
            income_total += amount
        elif t_type == "expense":
            expense_total += amount

        print(f"{timestamp} | {t_type:<7} | £{amount:.2f}")

    print("-" * 50)
    print(f"Income total : £{income_total:.2f}")
    print(f"Expense total: £{expense_total:.2f}")
    print(f"Net          : £{income_total - expense_total:.2f}\n")

def clear_all_data(filename=DATA_FILE):
    """Clear all transaction data safely."""
    confirm = input(
        "⚠️ This will delete ALL transaction data. Type 'YES' to confirm:\n> "
    ).strip()

    if confirm != "YES":
        print("Clear cancelled.")
        return

    # 1️⃣ Reset in-memory state
    finances["income"] = 0
    finances["expenses"] = 0
    finances["transactions"] = []

    # 2️⃣ Clear file safely (truncate)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            pass  # opening in "w" mode empties the file
    except OSError as e:
        print(f"Warning: could not clear file: {e}")
        return

    print("✅ All financial data has been cleared.")
def set_budget():
    pass

