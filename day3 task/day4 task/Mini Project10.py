# 10.number utility tool
# Concepts: Functions, Formatting
# Work with numbers.
# Requirements:
# Convert number to binary, octal, hex
# Format large numbers with commas
# Print scientific notation?

def convert_number(num):
    print(" Number Conversions:")
    print(f"Binary      : {bin(num)}")
    print(f"Octal       : {oct(num)}")
    print(f"Hexadecimal : {hex(num)}")

def format_number(num):
    print(" Formatted Number:")
    print(f"With commas: {num:,}")

def scientific_notation(num):
    print("\n🔬 Scientific Notation:")
    print(f"{num:.2e}")
while True:
    print("\n===== Number Utility Menu =====")
    print("1. Convert Number")
    print("2. Format Number")
    print("3. Scientific Notation")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice in ["1", "2", "3"]:
        num = int(input("Enter a number: "))
        
        if choice == "1":
            convert_number(num)
        elif choice == "2":
            format_number(num)
        elif choice == "3":
            scientific_notation(num)
    
    elif choice == "4":
        print(" Exiting tool")
        break
    else:
        print(" Invalid choice")
