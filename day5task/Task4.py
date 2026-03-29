# Task 4: Factorial Service (Recursion)
# Create:
# def factorial(n):
# Handle:
# n = 0
# negative numbers (show error)
def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("\nFactorial Results:")
while(1==1):
    n = input("Enter a number:")
    if(n == ""):
        break
    print(f"  factorial({int(n)}) = {factorial(int(n))}")