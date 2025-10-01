# -------------------------------------------
# Part 1: Group 10 Student A (Barbara K Zulu)
# -------------------------------------------

# Step 1: Variable definitions
incomes = []   # list to store incomes
expenses = []  # list to store expenses

# Step 2: Functions with input features
def add_income():
    """Function to add a new income"""
    amount = float(input("Enter income amount: "))
    incomes.append(amount)
    print(f"Income of {amount} added successfully!")

def add_expense():
    """Function to add a new expense"""
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)
    print(f"Expense of {amount} added successfully!")

# Step 3: Demonstration of Student A's part
print("---- Student A: Adding Incomes ----")
add_income()   # first income input
add_income()   # second income input

print("\n---- Student A: Adding Expenses ----")
add_expense()  # first expense input
add_expense()  # second expense input

# Step 4: Show current records
print("\n---- Current Records ----")
print("Incomes:", incomes)
print("Expenses:", expenses)
