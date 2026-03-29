# Task 2: Dynamic Calculator (*args)
# Create:
# def calculate_total(*numbers):
# Return sum of all numbers
# Accept unlimited inputs
# 👉 Bonus:
# Also return average
def calculate_total(*numbers):
    total = sum(numbers)  
    
    if len(numbers) > 0:
        average = total / len(numbers)
    else:
        average = 0
    
    return total, average


total, average = calculate_total(5, 7, 3, 6)

print("Total =", total)
print("Average =", average)
