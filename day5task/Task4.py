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
for n in [0, 5, 7, -3]:
    print(f"  factorial({n}) = {factorial(n)}")