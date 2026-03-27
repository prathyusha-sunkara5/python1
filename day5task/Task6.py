# Task 6: Exception Handling Module
# Take input:
# numerator
# denominator
# Handle:
# divide by zero
# invalid input
# 👉 Always print:
# Program Completed
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input (enter numbers only)")

finally:
    print("Program Completed")
    