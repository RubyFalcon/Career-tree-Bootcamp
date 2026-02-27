from datetime import datetime
import os
DATA_FILE = "transactions.txt"
BUDGET_FILE = "budget.txt"
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
            timestamp, t_type, category, amount = line.split("|")
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

def load_budget(filename=BUDGET_FILE):
    """Load monthly budget from file if it exists."""
    if not os.path.exists(filename):
        finances["monthly_budget"] = None
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            value = f.read().strip()
            finances["monthly_budget"] = float(value) if value else None
    except (ValueError, OSError):
        finances["monthly_budget"] = None

# save transactions
def save_transaction(transaction_type, category, converted_amount: float, filename=DATA_FILE, timestamp = None):
    """
    Appends a single transaction to a text file as pipe-delimited:
    timestamp|type|category|amount
    """
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp}|{transaction_type}|{category}|{converted_amount:.2f}\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(line)
    print(f"{transaction_type} of £{converted_amount:.2f} recorded successfully")
    return timestamp


MAX_INCOME  = 1_000_000
LARGE_TRANSACTION_THRESHOLD = 10_000
def add_income():
    """Add a new income transaction"""
    categories = ["salary", "freelance", "gift"]
    category = input("Category - Salary, Freelance, Gift:\n> ").lower().strip()

    try:
        if category not in categories:
            print("wrong input")
            return

        amount = input("Enter amount: £\n> ").strip()
        converted_amount = float(amount)

        if converted_amount <= 0:
            print("Amount was incorrect")
            return
        if converted_amount > MAX_INCOME:
            print(f"Amount must be £{MAX_INCOME:,.2f} or less.")
            return
        if converted_amount > LARGE_TRANSACTION_THRESHOLD:
            confirm = input(
            f"⚠️  This is a large income (£{converted_amount:,.2f}). Continue? (y/n): "
            ).strip().lower()

            if confirm not in ("y", "yes"):
                print("Income entry cancelled.")
                return

        
        # Save first, reuse the exact timestamp
        timestamp = save_transaction("income", category, converted_amount)

        # Update in-memory state
        finances["income"] += converted_amount
        finances["transactions"].append({
            "transaction_type": "income",
            "category": category,
            "amount": converted_amount,
            "timestamp": timestamp,
        })

    except ValueError:
        print("Invalid amount. Returning to menu")

def add_expense():
    """Add a new expense transaction"""
    categories = ["food", "transport", "bills"]
    category = input("Category - food, transport, bills:\n> ").lower().strip()

    try:
        if category not in categories:
            print("wrong input")
            return

        amount = input("Enter an amount: £\n> ").strip()
        converted_amount = float(amount)

        if converted_amount <= 0:
            print("Amount was incorrect")
            return

        # Save first and capture the exact timestamp used
        timestamp = save_transaction("expense", category, converted_amount)

        # Update in-memory state
        finances["expenses"] += converted_amount
        finances["transactions"].append({
            "transaction_type": "expense",
            "category": category,
            "amount": converted_amount,
            "timestamp": timestamp,
        })

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
    income = finances["income"]
    expenses = finances["expenses"]
    balance = income - expenses

    # ---- main summary ----
    print("\nFinancial Summary")
    print("-" * 40)

    print(f"{'Total Income:':<18} £{income:,.2f}")
    print(f"{'Total Expenses:':<18} £{expenses:,.2f}")
    print(f"{'Current Balance:':<18} £{balance:,.2f}")

    # ---- optional budget section ----
    budget = finances.get("monthly_budget")
    if budget is not None:
        remaining = budget - expenses
        print("-" * 40)
        print(f"{'Monthly Budget:':<18} £{budget:,.2f}")
        print(f"{'Budget Remaining:':<18} £{remaining:,.2f}")
        if remaining < 0:
            print("⚠️  You are over your monthly budget!")

    print()  # trailing newline
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
    # 1️ Reset in-memory state
    finances["income"] = 0
    finances["expenses"] = 0
    finances["transactions"] = []

    # 2️ Clear file safely (truncate)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            pass  # opening in "w" mode empties the file
    except OSError as e:
        print(f"Warning: could not clear file: {e}")
        return

    print("✅ All financial data has been cleared.")

def set_budget(filename=BUDGET_FILE):
    """Set or update the monthly budget."""
    try:
        amount = input("Enter monthly budget: £\n> ").strip()
        budget = float(amount)

        if budget <= 0:
            print("Budget must be greater than 0.")
            return

        # update memory
        finances["monthly_budget"] = budget

        # persist (overwrite — single source of truth)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{budget:.2f}")

        print(f"✅ Monthly budget set to £{budget:.2f}")

    except ValueError:
        print("Invalid budget amount.")

