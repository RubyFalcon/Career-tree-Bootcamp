# Personal Finance Tracker - Project

## 📋 Project Description
Build a command-line application to track your income and expenses. This project will help you understand how to build a complete Python application using functions, loops, and file operations.

## 🎯 What You'll Learn
- How to organize code with functions
- Working with files to save and load data
- Processing lists and dictionaries
- Building interactive menu systems
- Input validation and error handling

## ✨ Features to Implement

### Core Features
1. **Add Income** - Record money you receive
2. **Add Expense** - Record money you spend
3. **View All Transactions** - See your complete history
4. **View Summary** - See total income, expenses, and balance
5. **View by Category** - Group expenses by type

### Bonus Features (If you finish early)
6. **Set Budget** - Set a monthly spending limit
7. **Clear Data** - Reset all transactions
8. **Date Filtering** - View transactions from specific time periods

## 🚀 Getting Started

## 📝 How to Use

When you run the program, you'll see a menu:
```
1. Add Income
2. Add Expense
3. View All Transactions
4. View Summary
5. View by Category
6. Set Monthly Budget
7. Clear All Data
8. Exit
```

### Example Usage:

**Adding Income:**
```
Category: Salary
Amount: $3000
```

**Adding Expense:**
```
Category: Groceries
Amount: $150
```

**Viewing Summary:**
```
Total Income:    $3,000.00
Total Expenses:  $150.00
Current Balance: $2,850.00
```

## 📂 File Structure

The program creates two files:
- `transactions.txt` - Stores all your transactions
- `budget.txt` - Stores your monthly budget

### Transaction File Format:
```
2024-02-11 14:30:00|income|Salary|3000.00
2024-02-11 15:45:00|expense|Groceries|150.00
```

## 🛠️ Building the Project

### Step 1: Menu System (30 minutes)
Create the basic menu loop:
- Display menu options
- Get user input
- Use if/elif to handle choices
- Add exit option

### Step 2: Save Transactions (30 minutes)
Create functions to save data:
- `save_transaction()` - write to file
- `add_income()` - get user input and save
- `add_expense()` - get user input and save

### Step 3: Load and Display (45 minutes)
Create functions to read data:
- `load_transactions()` - read from file and parse
- `view_all_transactions()` - display all records

### Step 4: Calculate Summary (45 minutes)
Create analysis functions:
- `calculate_summary()` - total income/expenses
- `view_by_category()` - group by category

### Step 5: Polish (30 minutes)
Add finishing touches:
- Input validation
- Nice formatting
- Error handling
- Budget tracking


## 🎓 Learning Challenges

### Challenge 1: Input Validation
Make sure users can't enter negative amounts or invalid data.

### Challenge 2: Nice Formatting
Make your output look professional with aligned columns.

### Challenge 3: Category Totals
Use a dictionary to group expenses by category.

### Challenge 4: Budget Warning
Alert users when they exceed their budget.

## 🌟 Extension Ideas

1. **Search functionality** - Find transactions by keyword
2. **Edit transactions** - Modify or delete entries
3. **Monthly reports** - Show spending by month
4. **Categories presets** - Common categories to choose from
5. **Export to CSV** - Save in spreadsheet format

## 📚 What's Next?

After completing this project, you can:
- Convert it to a **Flask web app**
- Add a **database** (SQLite) instead of text files
- Create a **GUI** with Tkinter
- Add **data visualization** with charts
- Build an **API** for mobile apps

## 🏆 Success Checklist

- [ ] Menu displays and loops correctly
- [ ] Can add income transactions
- [ ] Can add expense transactions
- [ ] Transactions save to file
- [ ] Can view all transactions
- [ ] Summary calculations work
- [ ] Category breakdown works
- [ ] Input validation prevents crashes
- [ ] Code is organized into functions
- [ ] Added at least one custom feature

## 🤔 Questions to Think About

1. What happens if two people use this program?
2. How would you add support for multiple currencies?
3. How could you prevent duplicate transactions?
4. What would change if you used a database instead of files?

---

**Happy Coding! 💻**
