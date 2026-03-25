# 7. Bank Account System
# Concepts: Functions, Dictionary
# Simulate bank operations.
# Requirements:
# Create account (name, balance)
# Deposit money
# Withdraw money
# Check balance?

# Dictionary to store account details
account = {}

# Function to create account
def create_account():
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    
    account["name"] = name
    account["balance"] = balance
    
    print(" Account created successfully!")

# Function to deposit money
def deposit():
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        account["balance"] += amount
        print(f" Deposited ₹{amount}")
    else:
        print(" Invalid amount")

# Function to withdraw money
def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f" Withdrawn ₹{amount}")
    else:
        print(" Insufficient balance")

# Function to check balance
def check_balance():
    print(f" Account Holder: {account['name']}")
    print(f" Balance: ₹{account['balance']}")

# Menu-driven program
while True:
    print("\n===== Bank Menu =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print(" Thank you for using our bank system!")
        break
    else:
        print( "Invalid choice, try again.")